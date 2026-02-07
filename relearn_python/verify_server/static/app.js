/**
 * RELEARN-PYTHON - Application de vérification
 * Version ultra-épurée avec mode clair/sombre et vérification individuelle
 */

// État global
const appState = {
  chapterInfo: null,
  results: null,
  selectedExercise: null,
  solutionVisible: false,
  isLoading: false,
  currentTab: 'description',
  theme: localStorage.getItem('theme') || 'light'
};

// Éléments DOM
const elements = {};

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
  initializeTheme();
  initializeElements();
  setupEventListeners();
  loadInitialData();
});

// Gestion du thème
function initializeTheme() {
  if (appState.theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.removeAttribute('data-theme');
  }
  updateThemeButton();
}

function toggleTheme() {
  appState.theme = appState.theme === 'light' ? 'dark' : 'light';
  localStorage.setItem('theme', appState.theme);
  initializeTheme();
}

function updateThemeButton() {
  const icon = document.getElementById('theme-icon');
  const text = document.getElementById('theme-text');
  if (appState.theme === 'dark') {
    icon.textContent = '☀️';
    text.textContent = 'Clair';
  } else {
    icon.textContent = '🌙';
    text.textContent = 'Sombre';
  }
}

// Initialisation des éléments DOM
function initializeElements() {
  elements.chapterTitle = document.getElementById('chapter-title');
  elements.scorePassed = document.getElementById('score-passed');
  elements.scoreTotal = document.getElementById('score-total');
  elements.exercisesList = document.getElementById('exercises-list');
  elements.loadingState = document.getElementById('loading-state');
  elements.emptyState = document.getElementById('empty-state');
  elements.exerciseDetail = document.getElementById('exercise-detail');
  elements.globalError = document.getElementById('global-error');
  elements.globalErrorMessage = document.getElementById('global-error-message');
  
  // Detail view
  elements.detailTitle = document.getElementById('detail-title');
  elements.detailSubtitle = document.getElementById('detail-subtitle');
  elements.descriptionContent = document.getElementById('description-content');
  elements.userCode = document.getElementById('user-code');
  elements.solutionPanel = document.getElementById('solution-panel');
  elements.solutionCode = document.getElementById('solution-code');
  elements.suggestionCard = document.getElementById('suggestion-card');
  elements.suggestionText = document.getElementById('suggestion-text');
  elements.outputPanel = document.getElementById('output-panel');
  elements.outputContent = document.getElementById('output-content');
  elements.statusCard = document.getElementById('status-card');
  elements.statusIcon = document.getElementById('status-icon');
  elements.statusTitle = document.getElementById('status-title');
  elements.statusMessage = document.getElementById('status-message');
  
  // Buttons
  elements.themeToggle = document.getElementById('theme-toggle');
  elements.verifyAllBtn = document.getElementById('verify-all-btn');
  elements.btnShowSolution = document.getElementById('btn-show-solution');
  elements.btnVerifySingle = document.getElementById('btn-verify-single');
  elements.btnRerunAll = document.getElementById('btn-rerun-all');
  elements.btnCopyCode = document.getElementById('btn-copy-code');
  elements.btnCopySolution = document.getElementById('btn-copy-solution');
  
  // Tabs
  elements.tabs = document.querySelectorAll('.tab');
  elements.panels = document.querySelectorAll('.content-panel');
}

// Écouteurs d'événements
function setupEventListeners() {
  // Toggle theme
  elements.themeToggle.addEventListener('click', toggleTheme);
  
  // Vérifier tout
  elements.verifyAllBtn.addEventListener('click', runVerification);
  elements.btnRerunAll.addEventListener('click', runVerification);
  
  // Vérifier un seul
  elements.btnVerifySingle.addEventListener('click', verifySingleExercise);
  
  // Voir solution
  elements.btnShowSolution.addEventListener('click', toggleSolution);
  
  // Copier code
  elements.btnCopyCode.addEventListener('click', () => copyToClipboard('user-code'));
  elements.btnCopySolution.addEventListener('click', () => copyToClipboard('solution-code'));
  
  // Onglets
  elements.tabs.forEach(tab => {
    tab.addEventListener('click', () => switchTab(tab.dataset.tab));
  });
  
  // Raccourcis clavier
  document.addEventListener('keydown', (e) => {
    if (e.key === 'r' && e.ctrlKey) {
      e.preventDefault();
      if (appState.selectedExercise) {
        verifySingleExercise();
      }
    }
  });
}

// Charger les données initiales
async function loadInitialData() {
  showLoading();
  
  try {
    const chapterResponse = await fetch('/api/chapter-info');
    if (!chapterResponse.ok) throw new Error('Erreur chargement chapitre');
    appState.chapterInfo = await chapterResponse.json();
    
    elements.chapterTitle.textContent = appState.chapterInfo.title;
    
    await runVerification();
    
  } catch (error) {
    showGlobalError(error.message);
  }
}

// Vérification de tous les exercices
async function runVerification() {
  if (appState.isLoading) return;
  
  appState.isLoading = true;
  showLoading();
  
  try {
    const response = await fetch('/api/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Erreur de vérification');
    }
    
    appState.results = await response.json();
    
    updateScore();
    renderExercisesList();
    
    if (appState.results.exercises.length > 0) {
      const failedExercise = appState.results.exercises.find(ex => ex.status === 'failed');
      selectExercise(failedExercise || appState.results.exercises[0]);
    }
    
  } catch (error) {
    showGlobalError(error.message);
  } finally {
    appState.isLoading = false;
  }
}

// Vérification d'un seul exercice
async function verifySingleExercise() {
  if (!appState.selectedExercise || appState.isLoading) return;
  
  appState.isLoading = true;
  elements.btnVerifySingle.disabled = true;
  elements.btnVerifySingle.innerHTML = '<span class="icon">⏳</span> Vérification...';
  
  try {
    const exerciseNum = appState.selectedExercise.num;
    const response = await fetch(`/api/verify/${exerciseNum}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) throw new Error('Erreur de vérification');
    
    const result = await response.json();
    
    // Mettre à jour l'exercice dans les résultats
    const index = appState.results.exercises.findIndex(ex => ex.num === exerciseNum);
    if (index !== -1) {
      appState.results.exercises[index] = result;
    }
    
    // Mettre à jour l'UI
    updateScore();
    renderExercisesList();
    updateResultPanel(result);
    
    // Passer automatiquement à l'onglet résultat
    switchTab('result');
    
  } catch (error) {
    showGlobalError(error.message);
  } finally {
    appState.isLoading = false;
    elements.btnVerifySingle.disabled = false;
    elements.btnVerifySingle.innerHTML = '<span class="icon">▶</span> Vérifier cet exercice';
  }
}

// Mettre à jour le score
function updateScore() {
  const { passed, total } = appState.results;
  elements.scorePassed.textContent = passed;
  elements.scoreTotal.textContent = total;
}

// Afficher la liste des exercices
function renderExercisesList() {
  const list = elements.exercisesList;
  list.innerHTML = '';
  
  appState.results.exercises.forEach((exercise, index) => {
    const card = document.createElement('div');
    card.className = `exercise-card ${exercise.status}`;
    card.dataset.index = index;
    
    const statusIcon = exercise.status === 'passed' ? '✓' : 
                       exercise.status === 'failed' ? '✗' : '○';
    
    card.innerHTML = `
      <span class="exercise-number">${exercise.num}</span>
      <span class="exercise-name">${exercise.name}</span>
      <span class="exercise-status ${exercise.status}">${statusIcon}</span>
    `;
    
    card.addEventListener('click', () => selectExercise(exercise));
    list.appendChild(card);
  });
}

// Sélectionner un exercice
async function selectExercise(exercise) {
  appState.selectedExercise = exercise;
  appState.solutionVisible = false;
  
  // Mettre à jour la classe active
  document.querySelectorAll('.exercise-card').forEach(card => {
    card.classList.remove('active');
  });
  const activeCard = document.querySelector(`.exercise-card[data-index="${appState.results.exercises.indexOf(exercise)}"]`);
  if (activeCard) activeCard.classList.add('active');
  
  // Afficher le détail
  elements.loadingState.style.display = 'none';
  elements.emptyState.style.display = 'none';
  elements.globalError.style.display = 'none';
  elements.exerciseDetail.style.display = 'block';
  
  // Mettre à jour les infos
  elements.detailTitle.textContent = `Exercice ${exercise.num}`;
  elements.detailSubtitle.textContent = exercise.name;
  
  // Charger les données
  await Promise.all([
    loadDescription(exercise.num),
    loadExerciseCodes(exercise.num),
    updateResultPanel(exercise)
  ]);
  
  // Réinitialiser l'onglet
  switchTab('description');
}

// Charger la description
async function loadDescription(exerciseNum) {
  try {
    const response = await fetch(`/api/description/${exerciseNum}`);
    if (response.ok) {
      const description = await response.text();
      elements.descriptionContent.innerHTML = formatDescription(description);
    } else {
      elements.descriptionContent.innerHTML = '<p>Description non disponible</p>';
    }
  } catch (error) {
    elements.descriptionContent.innerHTML = '<p>Erreur de chargement</p>';
  }
}

// Formater la description (Markdown simple)
function formatDescription(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/```python\n([\s\S]+?)```/g, '<pre><code class="language-python">$1</code></pre>')
    .replace(/`(.+?)`/g, '<code>$1</code>');
}

// Charger les codes
async function loadExerciseCodes(exerciseNum) {
  try {
    // Code utilisateur
    const userResponse = await fetch(`/api/code/${exerciseNum}`);
    if (userResponse.ok) {
      const code = await userResponse.text();
      elements.userCode.textContent = code || '# Code non trouvé';
      highlightCode(elements.userCode);
    }
    
    // Solution
    const solutionResponse = await fetch(`/api/solution/${exerciseNum}`);
    if (solutionResponse.ok) {
      const solution = await solutionResponse.text();
      elements.solutionCode.textContent = solution || '# Solution non disponible';
      highlightCode(elements.solutionCode);
    }
    
    // Cacher la solution par défaut
    elements.solutionPanel.classList.add('hidden');
    elements.btnShowSolution.innerHTML = '<span class="icon">👁</span> Voir la solution';
    
  } catch (error) {
    console.error('Erreur chargement code:', error);
  }
}

// Mettre à jour le panneau de résultat
function updateResultPanel(exercise) {
  elements.statusCard.style.display = 'flex';
  elements.statusCard.className = `status-card ${exercise.status}`;
  
  if (exercise.status === 'passed') {
    elements.statusIcon.textContent = '✓';
    elements.statusTitle.textContent = 'Exercice réussi !';
    elements.statusTitle.style.color = 'var(--success)';
    elements.statusMessage.textContent = 'Bravo, votre solution est correcte.';
    elements.suggestionCard.style.display = 'none';
  } else {
    elements.statusIcon.textContent = '✗';
    elements.statusTitle.textContent = 'Exercice échoué';
    elements.statusTitle.style.color = 'var(--error)';
    elements.statusMessage.textContent = exercise.error_message || 'La solution ne produit pas le résultat attendu.';
    
    if (exercise.suggestion) {
      elements.suggestionCard.style.display = 'block';
      elements.suggestionText.textContent = exercise.suggestion;
    } else {
      elements.suggestionCard.style.display = 'none';
    }
  }
  
  if (exercise.output) {
    elements.outputPanel.style.display = 'block';
    elements.outputContent.textContent = exercise.output;
  } else {
    elements.outputPanel.style.display = 'none';
  }
}

// Basculer entre les onglets
function switchTab(tabName) {
  appState.currentTab = tabName;
  
  elements.tabs.forEach(tab => {
    tab.classList.toggle('active', tab.dataset.tab === tabName);
  });
  
  elements.panels.forEach(panel => {
    panel.classList.toggle('active', panel.id === `panel-${tabName}`);
  });
}

// Afficher/cacher la solution
function toggleSolution() {
  appState.solutionVisible = !appState.solutionVisible;
  
  if (appState.solutionVisible) {
    elements.solutionPanel.classList.remove('hidden');
    elements.btnShowSolution.innerHTML = '<span class="icon">🙈</span> Cacher la solution';
  } else {
    elements.solutionPanel.classList.add('hidden');
    elements.btnShowSolution.innerHTML = '<span class="icon">👁</span> Voir la solution';
  }
}

// Copier dans le presse-papiers
async function copyToClipboard(elementId) {
  const element = document.getElementById(elementId);
  const text = element.textContent;
  
  try {
    await navigator.clipboard.writeText(text);
    // Feedback visuel
    const btn = elementId === 'user-code' ? elements.btnCopyCode : elements.btnCopySolution;
    const originalText = btn.textContent;
    btn.textContent = '✓ Copié !';
    setTimeout(() => {
      btn.textContent = originalText;
    }, 2000);
  } catch (err) {
    console.error('Erreur copie:', err);
  }
}

// Syntax highlighting simple
function highlightCode(element) {
  let code = element.textContent;
  
  // Échapper HTML
  code = code.replace(/&/g, '&amp;')
             .replace(/</g, '&lt;')
             .replace(/>/g, '&gt;');
  
  // Keywords Python
  const keywords = ['def', 'return', 'if', 'else', 'elif', 'for', 'while', 'in', 'import', 'from', 'as', 'try', 'except', 'class', 'pass', 'True', 'False', 'None', 'print', 'input', 'float', 'int', 'str'];
  keywords.forEach(kw => {
    const regex = new RegExp(`\\b${kw}\\b`, 'g');
    code = code.replace(regex, `<span class="hljs-keyword">${kw}</span>`);
  });
  
  // Strings
  code = code.replace(/(".*?")/g, '<span class="hljs-string">$1</span>');
  code = code.replace(/('.*?')/g, '<span class="hljs-string">$1</span>');
  
  // Nombres
  code = code.replace(/\b(\d+(?:\.\d+)?)\b/g, '<span class="hljs-number">$1</span>');
  
  // Commentaires
  code = code.replace(/(#.*$)/gm, '<span class="hljs-comment">$1</span>');
  
  element.innerHTML = code;
}

// Afficher l'état de chargement
function showLoading() {
  elements.loadingState.style.display = 'flex';
  elements.emptyState.style.display = 'none';
  elements.exerciseDetail.style.display = 'none';
  elements.globalError.style.display = 'none';
}

// Afficher une erreur globale
function showGlobalError(message) {
  elements.loadingState.style.display = 'none';
  elements.emptyState.style.display = 'none';
  elements.exerciseDetail.style.display = 'none';
  elements.globalError.style.display = 'block';
  elements.globalErrorMessage.textContent = message;
}
