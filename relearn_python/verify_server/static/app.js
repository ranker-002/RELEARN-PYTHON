/**
 * RELEARN-PYTHON - Application de vérification
 * Version ultra-épurée avec mode clair/sombre et vérification individuelle
 */

console.log('[DEBUG] JavaScript file loaded');

if (typeof document !== 'undefined') {
  console.log('[DEBUG] Document is available');
  
  document.addEventListener('DOMContentLoaded', () => {
    console.log('[DEBUG] DOMContentLoaded fired');
    try {
      initializeTheme();
      initializeElements();
      setupEventListeners();
      loadInitialData();
      console.log('[DEBUG] Initialization complete');
    } catch (error) {
      console.error('[DEBUG] Initialization error:', error);
      showGlobalError('Erreur d\'initialisation: ' + error.message);
    }
  });
} else {
  console.log('[DEBUG] Document not available');
}

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
  console.log('[DEBUG] DOMContentLoaded fired');
  try {
    initializeTheme();
    initializeElements();
    setupEventListeners();
    loadInitialData();
    console.log('[DEBUG] Initialization complete');
  } catch (error) {
    console.error('[DEBUG] Initialization error:', error);
    showGlobalError('Erreur d\'initialisation: ' + error.message);
  }
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
  console.log('[DEBUG] initializeElements called');
  
  elements.chapterTitle = document.getElementById('chapter-title');
  elements.scorePassed = document.getElementById('score-passed');
  elements.scoreTotal = document.getElementById('score-total');
  elements.exercisesList = document.getElementById('exercises-list');
  elements.loadingState = document.getElementById('loading-state');
  elements.emptyState = document.getElementById('empty-state');
  elements.exerciseDetail = document.getElementById('exercise-detail');
  
  console.log('[DEBUG] Core elements:', {
    chapterTitle: !!elements.chapterTitle,
    scorePassed: !!elements.scorePassed,
    scoreTotal: !!elements.scoreTotal,
    exercisesList: !!elements.exercisesList,
    loadingState: !!elements.loadingState,
    emptyState: !!elements.emptyState,
    exerciseDetail: !!elements.exerciseDetail
  });
  
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
  
  console.log('[DEBUG] All elements initialized');
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
  console.log('[DEBUG] loadInitialData called');
  showLoading();
  
  try {
    console.log('[DEBUG] Fetching chapter info...');
    const chapterResponse = await fetch('/api/chapter-info');
    if (!chapterResponse.ok) throw new Error('Erreur chargement chapitre: ' + chapterResponse.status);
    appState.chapterInfo = await chapterResponse.json();
    console.log('[DEBUG] Chapter info:', appState.chapterInfo);
    
    if (elements.chapterTitle) {
      elements.chapterTitle.textContent = appState.chapterInfo.title;
    }
    
    console.log('[DEBUG] Running verification...');
    await runVerification();
    console.log('[DEBUG] Verification complete, results:', appState.results);
    
  } catch (error) {
    console.error('[DEBUG] Error:', error);
    showGlobalError(error.message || String(error));
  }
}

// Vérification de tous les exercices
async function runVerification() {
  if (appState.isLoading) {
    console.log('[DEBUG] Already loading, skipping...');
    return;
  }
  
  appState.isLoading = true;
  showLoading();
  
  try {
    console.log('[DEBUG] Fetching /api/verify...');
    const response = await fetch('/api/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || 'Erreur de vérification: ' + response.status);
    }
    
    appState.results = await response.json();
    console.log('[DEBUG] Verification results:', appState.results);
    
    updateScore();
    renderExercisesList();
    
    if (appState.results.exercises && appState.results.exercises.length > 0) {
      const failedExercise = appState.results.exercises.find(ex => ex.status === 'failed');
      selectExercise(failedExercise || appState.results.exercises[0]);
    } else {
      console.log('[DEBUG] No exercises found in results');
    }
    
  } catch (error) {
    console.error('[DEBUG] Verification error:', error);
    showGlobalError(error.message || String(error));
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
  console.log('[DEBUG] renderExercisesList called, exercises:', appState.results?.exercises?.length);
  const list = elements.exercisesList;
  list.innerHTML = '';
  
  if (!appState.results || !appState.results.exercises) {
    console.error('[DEBUG] No exercises to render');
    return;
  }
  
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
  console.log('[DEBUG] Rendered', list.children.length, 'exercises');
}

// Sélectionner un exercice
async function selectExercise(exercise) {
  console.log('[DEBUG] selectExercise called with:', exercise);
  appState.selectedExercise = exercise;
  appState.solutionVisible = false;
  
  // Mettre à jour la classe active
  document.querySelectorAll('.exercise-card').forEach(card => {
    card.classList.remove('active');
  });
  const activeCard = document.querySelector(`.exercise-card[data-index="${appState.results.exercises.indexOf(exercise)}"]`);
  if (activeCard) activeCard.classList.add('active');
  
  // Afficher le détail
  if (elements.loadingState) elements.loadingState.style.display = 'none';
  if (elements.emptyState) elements.emptyState.style.display = 'none';
  if (elements.exerciseDetail) elements.exerciseDetail.style.display = 'block';
  
  // Mettre à jour les infos
  if (elements.detailTitle) elements.detailTitle.textContent = `Exercice ${exercise.num}`;
  if (elements.detailSubtitle) elements.detailSubtitle.textContent = exercise.name;
  
  console.log('[DEBUG] Loading description, codes, and results...');
  
  // Charger les données
  await Promise.all([
    loadDescription(exercise.num),
    loadExerciseCodes(exercise.num),
    updateResultPanel(exercise)
  ]);
  
  console.log('[DEBUG] All data loaded, switching to description tab');
  
  // Réinitialiser l'onglet
  switchTab('description');
}

// Charger la description
async function loadDescription(exerciseNum) {
  console.log('[DEBUG] loadDescription called for:', exerciseNum);
  try {
    const response = await fetch(`/api/description/${exerciseNum}`);
    console.log('[DEBUG] Description response status:', response.status);
    if (response.ok) {
      const description = await response.text();
      console.log('[DEBUG] Description loaded:', description.substring(0, 100));
      if (elements.descriptionContent) {
        elements.descriptionContent.innerHTML = formatDescription(description);
      }
    } else {
      console.log('[DEBUG] Description not found');
      if (elements.descriptionContent) {
        elements.descriptionContent.innerHTML = '<p>Description non disponible</p>';
      }
    }
  } catch (error) {
    console.error('[DEBUG] Error loading description:', error);
    if (elements.descriptionContent) {
      elements.descriptionContent.innerHTML = '<p>Erreur de chargement</p>';
    }
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
  console.log('[DEBUG] loadExerciseCodes CALLED for:', exerciseNum);
  try {
    // Code utilisateur
    const userResponse = await fetch(`/api/code/${exerciseNum}`);
    console.log('[DEBUG] userResponse.status:', userResponse.status);
    if (userResponse.ok) {
      const code = await userResponse.text();
      console.log('[DEBUG] code loaded:', code.substring(0, 50));
      if (elements.userCode) {
        renderCode(elements.userCode, code);
      }
    }
    
    // Solution
    const solutionResponse = await fetch(`/api/solution/${exerciseNum}`);
    console.log('[DEBUG] solutionResponse.status:', solutionResponse.status);
    if (solutionResponse.ok) {
      const solution = await solutionResponse.text();
      console.log('[DEBUG] solution loaded:', solution.substring(0, 50));
      if (elements.solutionCode) {
        renderCode(elements.solutionCode, solution);
      }
    }
    
    // Cacher la solution par défaut
    if (elements.solutionPanel) elements.solutionPanel.classList.add('hidden');
    if (elements.btnShowSolution) {
      elements.btnShowSolution.innerHTML = '<span class="icon">👁</span> Voir la solution';
    }
    
  } catch (error) {
    console.error('[DEBUG] Error loading codes:', error);
  }
}

// Syntax highlighting - approche DOM directe
function renderCode(element, code) {
  if (!code) return;
  
  // Vider l'élément
  element.innerHTML = '';
  
  // Parser le code ligne par ligne
  const lines = code.split('\n');
  
  lines.forEach((line, lineIndex) => {
    // Créer un conteneur pour chaque ligne
    const lineDiv = document.createElement('div');
    lineDiv.style.whiteSpace = 'pre';
    lineDiv.style.fontFamily = 'var(--font-mono)';
    lineDiv.style.fontSize = '14px';
    lineDiv.style.lineHeight = '1.6';
    lineDiv.style.marginBottom = '4px';
    
    // Parser la ligne pour les spans
    let i = 0;
    while (i < line.length) {
      const char = line[i];
      
      // Commentaire
      if (char === '#') {
        const span = document.createElement('span');
        span.className = 'c';
        span.textContent = line.substring(i);
        lineDiv.appendChild(span);
        break;
      }
      
      // String guillemets doubles
      if (char === '"' && (i === 0 || line[i-1] !== '\\')) {
        let str = char;
        i++;
        while (i < line.length && (line[i] !== '"' || line[i-1] === '\\')) {
          str += line[i];
          i++;
        }
        if (i < line.length) str += line[i];
        i++;
        const span = document.createElement('span');
        span.className = 's';
        span.textContent = str;
        lineDiv.appendChild(span);
        continue;
      }
      
      // String guillemets simples
      if (char === "'" && (i === 0 || line[i-1] !== '\\')) {
        let str = char;
        i++;
        while (i < line.length && (line[i] !== "'" || line[i-1] === '\\')) {
          str += line[i];
          i++;
        }
        if (i < line.length) str += line[i];
        i++;
        const span = document.createElement('span');
        span.className = 's';
        span.textContent = str;
        lineDiv.appendChild(span);
        continue;
      }
      
      // Mot-clé Python
      const keywords = ['def', 'return', 'if', 'else', 'elif', 'for', 'while', 'in', 'import', 'from', 'as', 'try', 'except', 'class', 'pass', 'True', 'False', 'None', 'print', 'input', 'float', 'int', 'str'];
      let match = false;
      for (const kw of keywords) {
        const regex = new RegExp('^' + kw + '\\b');
        if (regex.test(line.substring(i))) {
          const span = document.createElement('span');
          span.className = 'k';
          span.textContent = kw;
          lineDiv.appendChild(span);
          i += kw.length;
          match = true;
          break;
        }
      }
      if (match) continue;
      
      // Nombre
      const numRegex = /^(\d+(?:\.\d+)?)/;
      const numMatch = line.substring(i).match(numRegex);
      if (numMatch) {
        const span = document.createElement('span');
        span.className = 'n';
        span.textContent = numMatch[1];
        lineDiv.appendChild(span);
        i += numMatch[1].length;
        continue;
      }
      
      // Caractère normal
      const span = document.createElement('span');
      span.textContent = char;
      span.style.color = 'inherit';
      lineDiv.appendChild(span);
      i++;
    }
    
    element.appendChild(lineDiv);
  });
}

// Mettre à jour le panneau de résultat
function updateResultPanel(exercise) {
  console.log('[DEBUG] updateResultPanel called with:', exercise);
  if (!exercise) {
    console.log('[DEBUG] Exercise is null or undefined');
    return;
  }
  
  if (elements.statusCard) {
    elements.statusCard.style.display = 'flex';
    elements.statusCard.className = `status-card ${exercise.status}`;
  }
  
  if (exercise.status === 'passed') {
    if (elements.statusIcon) elements.statusIcon.textContent = '✓';
    if (elements.statusTitle) {
      elements.statusTitle.textContent = 'Exercice réussi !';
      elements.statusTitle.style.color = 'var(--success)';
    }
    if (elements.statusMessage) elements.statusMessage.textContent = 'Bravo, votre solution est correcte.';
    if (elements.suggestionCard) elements.suggestionCard.style.display = 'none';
  } else {
    if (elements.statusIcon) elements.statusIcon.textContent = '✗';
    if (elements.statusTitle) {
      elements.statusTitle.textContent = 'Exercice échoué';
      elements.statusTitle.style.color = 'var(--error)';
    }
    if (elements.statusMessage) elements.statusMessage.textContent = exercise.error_message || 'La solution ne produit pas le résultat attendu.';
    
    if (exercise.suggestion && elements.suggestionCard) {
      elements.suggestionCard.style.display = 'block';
      if (elements.suggestionText) elements.suggestionText.textContent = exercise.suggestion;
    } else if (elements.suggestionCard) {
      elements.suggestionCard.style.display = 'none';
    }
  }
  
  if (exercise.output && elements.outputPanel) {
    elements.outputPanel.style.display = 'block';
    if (elements.outputContent) elements.outputContent.textContent = exercise.output;
  } else if (elements.outputPanel) {
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

// Afficher l'état de chargement
function showLoading() {
  if (elements.loadingState) elements.loadingState.style.display = 'flex';
  if (elements.emptyState) elements.emptyState.style.display = 'none';
  if (elements.exerciseDetail) elements.exerciseDetail.style.display = 'none';
}

// Afficher une erreur globale
function showGlobalError(message) {
  if (elements.loadingState) elements.loadingState.style.display = 'none';
  if (elements.emptyState) {
    elements.emptyState.style.display = 'flex';
    elements.emptyState.innerHTML = `
      <div class="empty-icon" aria-hidden="true">❌</div>
      <div class="empty-title">Erreur</div>
      <div class="empty-text">${message}</div>
    `;
  }
  if (elements.exerciseDetail) elements.exerciseDetail.style.display = 'none';
}
