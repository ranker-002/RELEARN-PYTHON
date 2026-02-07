#!/usr/bin/env python3
"""
Calculatrice CLI - Effectuez des calculs mathématiques en ligne de commande.

Usage:
    python src/main.py                    # Mode interactif
    python src/main.py --expr "2 + 3"     # Calcul direct
    python src/main.py --convert 100 C F # Conversion
    python src/main.py --history         # Afficher l'historique
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime


try:
    from .models.operation import TypeOperation, Operation, Calcul, Variable
    from .models.historique import Historique
    from .models.variable import GestionnaireVariables
    from .services.calculateur import Calculateur
    from .services.convertisseur import Convertisseur
    from .services.evaluateur import Evaluateur
    from .utils.config import Config
    from .utils.formatter import ResultFormatter
except ImportError:
    from models.operation import TypeOperation, Operation, Calcul, Variable
    from models.historique import Historique
    from models.variable import GestionnaireVariables
    from services.calculateur import Calculateur
    from services.convertisseur import Convertisseur
    from services.evaluateur import Evaluateur
    from utils.config import Config
    from utils.formatter import ResultFormatter


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"


class CalculatriceApp:
    VERSION = "1.0.0"
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = Config(config_path) if config_path else Config()
        self.calculateur = Calculateur()
        self.convertisseur = Convertisseur()
        self.evaluateur = Evaluateur()
        self.historique = Historique()
        self.variables = GestionnaireVariables()
        
        self.page_courante = 1
        self.resultats_par_page = 10
        
        self._afficher_banniere()
    
    def _afficher_banniere(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}")
        print("╔══════════════════════════════════════════════════╗")
        print("║              CALCULATRICE CLI                  ║")
        print("╠══════════════════════════════════════════════════╣")
        print(f"║  Version: {self.VERSION:<37}║")
        print(f"║  Précision: {self.config.get_precision():<33}║")
        print("╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def _afficher_menu(self):
        print(f"\n{Colors.BOLD}Menu Principal:{Colors.RESET}")
        print("  1. Calcul simple")
        print("  2. Calcul avancé")
        print("  3. Conversion d'unités")
        print("  4. Historique")
        print("  5. Variables")
        print("  6. Aide")
        print("  7. Quitter")
        print()
    
    def _calculer(self, expression: str) -> tuple[float, bool, Optional[str]]:
        """Effectue un calcul."""
        try:
            resultat, valide, erreur = self.evaluateur.evaluer(expression)
            self.historique.ajouter_expression(expression, resultat, valide, erreur)
            return resultat, valide, erreur
        except Exception as e:
            return 0.0, False, str(e)
    
    def _convertir(self, valeur: float, source: str, cible: str, categorie: str) -> tuple[float, Optional[str]]:
        """Effectue une conversion."""
        try:
            resultat = self.convertisseur.convertir(valeur, source, cible, categorie)
            return resultat, None
        except Exception as e:
            return 0.0, str(e)
    
    def mode_interactif(self):
        """Lance le mode interactif."""
        print(f"{Colors.YELLOW}Entrez vos calculs (ex: '2 + 3 * 4'){Colors.RESET}")
        print(f"{Colors.YELLOW}Tapez 'help' pour l'aide, 'quit' pour quitter{Colors.RESET}")
        
        while True:
            try:
                expression = input(f"\n{Colors.BOLD}calc>{Colors.RESET} ").strip()
                
                if not expression:
                    continue
                
                expression_lower = expression.lower()
                
                if expression_lower in ['quit', 'exit', 'q', 'sortir']:
                    print(f"\n{Colors.CYAN}Au revoir!{Colors.RESET}")
                    break
                
                elif expression_lower in ['help', 'aide', '?']:
                    self._afficher_aide()
                
                elif expression_lower == 'history':
                    self._afficher_historique()
                
                elif expression_lower.startswith('var '):
                    self._gerer_variable(expression)
                
                elif expression_lower in ['vars', 'variables']:
                    self._lister_variables()
                
                elif expression_lower.startswith('convert '):
                    self._traitement_conversion(expression)
                
                elif expression_lower in ['config', 'settings']:
                    self._afficher_config()
                
                elif expression_lower == 'clear':
                    self.historique.effacer()
                    print(f"{Colors.GREEN}Historique effacé.{Colors.RESET}")
                
                else:
                    resultat, valide, erreur = self._calculer(expression)
                    
                    if valide:
                        precision = self.config.get_precision()
                        resultat_str = ResultFormatter.formater_nombre(resultat, precision)
                        print(f"\n{Colors.GREEN}Résultat: {Colors.BOLD}{resultat_str}{Colors.RESET}")
                    else:
                        print(f"\n{Colors.RED}Erreur: {erreur}{Colors.RESET}")
            
            except (EOFError, KeyboardInterrupt):
                print(f"\n\n{Colors.CYAN}Au revoir!{Colors.RESET}")
                break
    
    def _afficher_aide(self):
        print(f"\n{Colors.BOLD}Aide de la Calculatrice{Colors.RESET}")
        print("-" * 50)
        print(f"{Colors.CYAN}Opérations de base:{Colors.RESET}")
        print("  +, -, *, /        Addition, soustraction, multiplication, division")
        print("  ^                 Puissance (ex: 2^3 = 8)")
        print("  %                 Modulo (ex: 10 % 3 = 1)")
        print()
        print(f"{Colors.CYAN}Fonctions avancées:{Colors.RESET}")
        print("  sqrt(x)           Racine carrée")
        print("  abs(x)            Valeur absolue")
        print("  floor(x)          Arrondi inférieur")
        print("  ceil(x)           Arrondi supérieur")
        print("  sin(x), cos(x)    Sinus, cosinus (en degrés)")
        print("  log(x)            Logarithme base 10")
        print("  ln(x)             Logarithme naturel")
        print("  fact(x)           Factorielle")
        print()
        print(f"{Colors.CYAN}Conversions:{Colors.RESET}")
        print("  convert VALEUR SOURCE CIBLE [CATÉGORIE]")
        print("  Ex: convert 100 C F (Celsius vers Fahrenheit)")
        print("  Ex: convert 1 km m (kilomètres vers mètres)")
        print()
        print(f"{Colors.CYAN}Variables:{Colors.RESET}")
        print("  var x = 10        Définir une variable")
        print("  x                 Utiliser une variable")
        print("  vars              Lister les variables")
        print()
        print(f"{Colors.CYAN}Commandes:{Colors.RESET}")
        print("  history           Afficher l'historique")
        print("  clear             Effacer l'historique")
        print("  config            Afficher la configuration")
        print("  quit              Quitter")
    
    def _afficher_historique(self):
        print(f"\n{Colors.BOLD}Historique des calculs{Colors.RESET}")
        print("-" * 50)
        historique = self.historique.afficher(20)
        print(historique)
        print("-" * 50)
        stats = self.historique.get_statistiques()
        print(f"{Colors.CYAN}Total: {stats['total']} | Valides: {stats['valides']} | Erreurs: {stats['erreurs']}{Colors.RESET}")
    
    def _gerer_variable(self, expression: str):
        """Gère la définition de variables."""
        try:
            if '=' in expression:
                _, reste = expression.split('=', 1)
                reste = reste.strip()
                if ' = ' in reste:
                    nom, val_str = reste.split(' = ', 1)
                    nom = nom.strip()
                    val_str = val_str.strip()
                else:
                    parties = reste.split()
                    nom = parties[0]
                    val_str = ' '.join(parties[1:]) if len(parties) > 1 else '0'
                
                if nom in ['+', '-', '*', '/', '^']:
                    print(f"{Colors.RED}Nom de variable invalide{Colors.RESET}")
                    return
                
                resultat, valide, erreur = self._calculer(val_str)
                if valide:
                    self.variables.ajouter(nom, resultat)
                    print(f"{Colors.GREEN}Variable '{nom}' définie: {resultat}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}Erreur: {erreur}{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}Erreur: {e}{Colors.RESET}")
    
    def _lister_variables(self):
        """Liste les variables définies."""
        print(f"\n{Colors.BOLD}Variables définies{Colors.RESET}")
        print("-" * 50)
        vars_list = self.variables.lister()
        if vars_list:
            for var in vars_list:
                print(f"  {var.nom} = {var.valeur}")
        else:
            print("  Aucune variable définie.")
        print("-" * 50)
    
    def _traitement_conversion(self, expression: str):
        """Traite une commande de conversion."""
        try:
            parties = expression.split()[1:]
            if len(parties) < 3:
                print(f"{Colors.RED}Usage: convert VALEUR SOURCE CIBLE [CATÉGORIE]{Colors.RESET}")
                return
            
            valeur = float(parties[0])
            source = parties[1]
            cible = parties[2]
            categorie = parties[3] if len(parties) > 3 else 'longueur'
            
            resultat, erreur = self._convertir(valeur, source, cible, categorie)
            
            if erreur:
                print(f"{Colors.RED}Erreur: {erreur}{Colors.RESET}")
            else:
                precision = self.config.get_precision()
                resultat_str = ResultFormatter.formater_nombre(resultat, precision)
                print(f"\n{Colors.GREEN}{valeur} {source} = {resultat_str} {cible}{Colors.RESET}")
        
        except ValueError:
            print(f"{Colors.RED}Valeur invalide{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}Erreur: {e}{Colors.RESET}")
    
    def _afficher_config(self):
        """Affiche la configuration actuelle."""
        print(f"\n{Colors.BOLD}Configuration{Colors.RESET}")
        print("-" * 50)
        print(f"  Précision: {self.config.get_precision()} décimales")
        print(f"  Notation: {self.config.get_notation()}")
        print(f"  Mode: {self.config.get_mode()}")
        print(f"  Thème: {self.config.get_theme()}")
        print("-" * 50)
    
    def _traiter_arguments(self):
        """Traite les arguments de ligne de commande."""
        parser = argparse.ArgumentParser(
            description="Calculatrice CLI - Effectuez des calculs mathématiques",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Exemples:
    python src/main.py                              # Mode interactif
    python src/main.py --expr "2 + 3 * 4"         # Calcul direct
    python src/main.py --expr "sqrt(16)"           # Fonction mathématique
    python src/main.py --convert 100 C F           # Conversion température
    python src/main.py --convert 1 km m            # Conversion longueur
    python src/main.py --history                   # Afficher l'historique
    python src/main.py --vars                      # Lister les variables
            """
        )
        parser.add_argument("--expr", "-e", metavar="EXPRESSION",
                           help="Expression à calculer")
        parser.add_argument("--convert", "-c", nargs="+", metavar=("VALEUR", "SOURCE", "CIBLE", "CAT"),
                           help="Convertir des unités")
        parser.add_argument("--history", "-H", action="store_true",
                           help="Afficher l'historique")
        parser.add_argument("--vars", "-v", action="store_true",
                           help="Lister les variables")
        parser.add_argument("--clear", action="store_true",
                           help="Effacer l'historique")
        parser.add_argument("--precision", "-p", type=int, metavar="N",
                           help="Définir la précision")
        parser.add_argument("--version", action="version",
                           version=f"%(prog)s {self.VERSION}")
        
        args = parser.parse_args()
        
        if args.clear:
            self.historique.effacer()
            print(f"{Colors.GREEN}Historique effacé.{Colors.RESET}")
        
        elif args.precision:
            self.config.set_precision(args.precision)
            print(f"{Colors.GREEN}Précision définie à {args.precision} décimales.{Colors.RESET}")
        
        elif args.vars:
            self._lister_variables()
        
        elif args.history:
            self._afficher_historique()
        
        elif args.convert:
            try:
                valeur = float(args.convert[0])
                source = args.convert[1]
                cible = args.convert[2]
                categorie = args.convert[3] if len(args.convert) > 3 else 'longueur'
                
                resultat, erreur = self._convertir(valeur, source, cible, categorie)
                
                if erreur:
                    print(f"{Colors.RED}Erreur: {erreur}{Colors.RESET}")
                else:
                    precision = self.config.get_precision()
                    resultat_str = ResultFormatter.formater_nombre(resultat, precision)
                    print(f"{valeur} {source} = {resultat_str} {cible}")
            
            except ValueError:
                print(f"{Colors.RED}Usage: --convert VALEUR SOURCE CIBLE [CATÉGORIE]{Colors.RESET}")
        
        elif args.expr:
            resultat, valide, erreur = self._calculer(args.expr)
            
            if valide:
                precision = self.config.get_precision()
                resultat_str = ResultFormatter.formater_nombre(resultat, precision)
                print(f"{resultat_str}")
            else:
                print(f"{Colors.RED}Erreur: {erreur}{Colors.RESET}")
                sys.exit(1)
        
        else:
            self.mode_interactif()
    
    def run(self):
        """Point d'entrée principal."""
        if len(sys.argv) > 1:
            self._traiter_arguments()
        else:
            self.mode_interactif()


def main():
    app = CalculatriceApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}Au revoir!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
