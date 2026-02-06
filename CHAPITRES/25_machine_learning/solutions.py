# =============================================================================
# CHAPITRE 25: MACHINE LEARNING - SOLUTIONS
# =============================================================================

# =============================================================================
# EXERCICE 25.1 - RÉGRESSION LINÉAIRE SIMPLE
# =============================================================================
def exercice_25_1():
    from sklearn.linear_model import LinearRegression
    import numpy as np

    X = np.array([[50], [60], [70], [80], [90], [100]])
    y = np.array([100000, 120000, 140000, 160000, 180000, 200000])

    model = LinearRegression()
    model.fit(X, y)

    prix = model.predict([[75]])
    print(f"Prix prédit pour 75m²: {prix[0]:,.0f} €")
    print(f"Coefficient: {model.coef_[0]:,.0f} €/m²")
    print(f"Intercept: {model.intercept_:,.0f} €")


# =============================================================================
# EXERCICE 25.2 - ÉVALUATION R² SCORE
# =============================================================================
def exercice_25_2():
    from sklearn.metrics import r2_score
    import numpy as np

    X = np.array([[50], [60], [70], [80], [90], [100]])
    y = np.array([100000, 120000, 140000, 160000, 180000, 200000])

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    print(f"R² Score: {r2:.4f}")


# =============================================================================
# EXERCICE 25.3 - RÉGRESSION MULTIPLE
# =============================================================================
def exercice_25_3():
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    df = pd.DataFrame({
        'surface': [50, 60, 70, 80, 90, 100, 110, 120],
        'chambres': [2, 2, 3, 3, 3, 4, 4, 4],
        'age': [10, 5, 15, 8, 2, 5, 1, 0],
        'prix': [100000, 120000, 140000, 160000, 180000, 200000, 210000, 230000]
    })

    X = df[['surface', 'chambres', 'age']]
    y = df['prix']

    model = LinearRegression()
    model.fit(X, y)

    nouvelle_maison = [[75, 3, 5]]  # surface, chambres, age
    prix = model.predict(nouvelle_maison)
    print(f"Prix prédit: {prix[0]:,.0f} €")

    print("\nImpact des features:")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"  {feature}: {coef:,.0f} €/unité")


# =============================================================================
# EXERCICE 25.4 - RÉGRESSION LOGISTIQUE
# =============================================================================
def exercice_25_4():
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    X, y = make_classification(n_samples=100, n_features=20, n_informative=5,
                               n_redundant=10, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Précision: {accuracy:.2%}")


# =============================================================================
# EXERCICE 25.5 - KNN
# =============================================================================
def exercice_25_5():
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    accuracy = knn.score(X_test, y_test)
    print(f"Précision KNN: {accuracy:.2%}")

    nouvelle_fleur = [[5.1, 3.5, 1.4, 0.2]]
    prediction = knn.predict(nouvelle_fleur)
    print(f"Espèce prédite: {iris.target_names[prediction[0]]}")


# =============================================================================
# EXERCICE 25.6 - ARBRE DE DÉCISION
# =============================================================================
def exercice_25_6():
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

    arbre = DecisionTreeClassifier(max_depth=3)
    arbre.fit(X_train, y_train)

    accuracy = arbre.score(X_test, y_test)
    print(f"Précision: {accuracy:.2%}")

    print("\nImportance des features:")
    for feature, importance in zip(iris.feature_names, arbre.feature_importances_):
        if importance > 0:
            print(f"  {feature}: {importance:.3f}")


# =============================================================================
# EXERCICE 25.7 - RANDOM FOREST
# =============================================================================
def exercice_25_7():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    dt = DecisionTreeClassifier(max_depth=5)
    dt.fit(X_train, y_train)
    print(f"Decision Tree: {dt.score(X_test, y_test):.2%}")

    rf = RandomForestClassifier(n_estimators=100, max_depth=5)
    rf.fit(X_train, y_train)
    print(f"Random Forest: {rf.score(X_test, y_test):.2%}")


# =============================================================================
# EXERCICE 25.8 - K-MEANS
# =============================================================================
def exercice_25_8():
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs
    import matplotlib.pyplot as plt

    X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    labels = kmeans.predict(X)
    centers = kmeans.cluster_centers_

    print(f"Clusters trouvés: {len(centers)}")
    print(f"Nombre de points: {len(labels)}")

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')
    plt.title('K-Means Clustering')
    plt.show()


# =============================================================================
# EXERCICE 25.9 - VALIDATION CROISÉE
# =============================================================================
def exercice_25_9():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import cross_val_score

    iris = load_iris()
    X, y = iris.data, iris.target

    rf = RandomForestClassifier(n_estimators=100)

    scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')

    print(f"Scores par fold: {[f'{s:.2%}' for s in scores]}")
    print(f"Moyenne: {scores.mean():.2%} ± {scores.std():.2%}")


# =============================================================================
# EXERCICE 25.10 - PRÉTRAITEMENT
# =============================================================================
def exercice_25_10():
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.datasets import load_iris

    iris = load_iris()
    X = iris.data

    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)

    normalizer = MinMaxScaler()
    X_norm = normalizer.fit_transform(X)

    print("Données originales - Min: ", X.min(axis=0)[:3])
    print("Données originales - Max: ", X.max(axis=0)[:3])
    print("\nStandardisées - Moyenne: ", X_std.mean(axis=0)[:3].round(4))
    print("Standardisées - Std: ", X_std.std(axis=0)[:3].round(4))
    print("\nNormalisées - Min: ", X_norm.min(axis=0)[:3].round(4))
    print("Normalisées - Max: ", X_norm.max(axis=0)[:3].round(4))


# =============================================================================
# EXERCICE 25.11 - PIPELINE
# =============================================================================
def exercice_25_11():
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import load_iris

    iris = load_iris()
    X, y = iris.data, (iris.target != 0).astype(int)

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression())
    ])

    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(pipeline, X, y, cv=5)
    print(f"Pipeline accuracy: {scores.mean():.2%} ± {scores.std():.2%}")


# =============================================================================
# EXERCICE 25.12 - MATRICE DE CONFUSION
# =============================================================================
def exercice_25_12():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns

    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    print("Matrice de confusion:")
    print(cm)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=iris.target_names,
                yticklabels=iris.target_names)
    plt.title('Matrice de Confusion')
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.show()


# =============================================================================
# EXERCICE 25.13 - ROC AUC
# =============================================================================
def exercice_25_13():
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score, roc_curve
    import matplotlib.pyplot as plt

    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_proba = model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_proba)
    print(f"ROC-AUC Score: {roc_auc:.4f}")

    fpr, tpr, _ = roc_curve(y_test, y_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.3f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()


# =============================================================================
# EXERCICE 25.14 - FEATURE SELECTION
# =============================================================================
def exercice_25_14():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_breast_cancer

    cancer = load_breast_cancer()
    X, y = cancer.data, cancer.target

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)

    importances = dict(zip(cancer.feature_names, rf.feature_importances_))
    top_10 = sorted(importances.items(), key=lambda x: x[1], reverse=True)[:10]

    print("Top 10 features les plus importantes:")
    for feature, importance in top_10:
        print(f"  {feature}: {importance:.4f}")


# =============================================================================
# EXERCICE 25.15 - PROJET COMPLET
# =============================================================================
def exercice_25_15():
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    import numpy as np

    # Générer des données immobilières réalistes
    np.random.seed(42)
    n_samples = 500

    surface = np.random.normal(80, 30, n_samples)
    surface = np.clip(surface, 20, 200)

    chambres = np.random.choice([1, 2, 3, 4, 5], n_samples,
                               p=[0.05, 0.20, 0.40, 0.25, 0.10])

    age = np.random.exponential(10, n_samples)
    age = np.clip(age, 0, 50)

    prix = (surface * 2000 + 
            chambres * 15000 - 
            age * 500 + 
            np.random.normal(0, 10000, n_samples))

    df = np.column_stack([surface, chambres, age, prix])

    X = df[:, :3]
    y = df[:, 3]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Comparer modèles
    models = {
        'LinearRegression': LinearRegression(),
        'RandomForest': RandomForestRegressor(n_estimators=100),
        'GradientBoosting': GradientBoostingRegressor(n_estimators=100)
    }

    print("Comparaison des modèles:")
    print("-" * 50)
    best_model = None
    best_score = 0

    for name, model in models.items():
        # Validation croisée
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        model.fit(X_train, y_train)
        test_score = model.score(X_test, y_test)

        print(f"{name}:")
        print(f"  CV R²: {scores.mean():.3f} ± {scores.std():.3f}")
        print(f"  Test R²: {test_score:.3f}")

        if test_score > best_score:
            best_score = test_score
            best_model = (name, model)

    print(f"\nMeilleur modèle: {best_model[0]} (R² = {best_score:.3f})")

    # Prédiction
    maison = [[75, 3, 5]]
    prix_predit = best_model[1].predict(maison)[0]
    print(f"\nPrix prédit pour 75m², 3 chambres, 5 ans: {prix_predit:,.0f} €")
