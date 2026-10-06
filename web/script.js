// Configuration
const API_URL = 'http://localhost:8000';

// DOM Elements
const form = document.getElementById('predictionForm');
const submitBtn = document.getElementById('submitBtn');
const resetBtn = document.getElementById('resetBtn');
const loadingOverlay = document.getElementById('loadingOverlay');
const resultCard = document.getElementById('resultCard');
const closeResult = document.getElementById('closeResult');
const newEvaluation = document.getElementById('newEvaluation');
const apiStatus = document.getElementById('apiStatus');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initializeQuestionToggles();
    checkAPIStatus();
    setupEventListeners();
});

// Check API Status
async function checkAPIStatus() {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (response.ok) {
            apiStatus.classList.add('online');
            apiStatus.querySelector('span').textContent = 'API Conectada';
        } else {
            throw new Error('API no disponible');
        }
    } catch (error) {
        apiStatus.classList.add('offline');
        apiStatus.querySelector('span').textContent = 'API Desconectada';
        console.error('Error checking API status:', error);
    }
}

// Initialize Question Toggles
function initializeQuestionToggles() {
    const questionItems = document.querySelectorAll('.question-item');
    
    questionItems.forEach(item => {
        const toggleBtns = item.querySelectorAll('.toggle-btn');
        const hiddenInput = item.querySelector('input[type="hidden"]');
        
        toggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active from all buttons in this question
                toggleBtns.forEach(b => b.classList.remove('active'));
                
                // Add active to clicked button
                btn.classList.add('active');
                
                // Set value
                const value = btn.dataset.value;
                hiddenInput.value = value;
                
                // Add animation
                btn.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    btn.style.transform = '';
                }, 200);
            });
        });
    });
}

// Setup Event Listeners
function setupEventListeners() {
    form.addEventListener('submit', handleSubmit);
    resetBtn.addEventListener('click', handleReset);
    closeResult.addEventListener('click', hideResult);
    newEvaluation.addEventListener('click', handleNewEvaluation);
}

// Handle Form Submit
async function handleSubmit(e) {
    e.preventDefault();
    
    // Validate all questions are answered
    const allQuestions = document.querySelectorAll('.question-item input[type="hidden"]');
    let allAnswered = true;
    
    allQuestions.forEach(input => {
        if (!input.value) {
            allAnswered = false;
            const questionItem = input.closest('.question-item');
            questionItem.style.borderColor = 'var(--danger)';
            setTimeout(() => {
                questionItem.style.borderColor = '';
            }, 2000);
        }
    });
    
    if (!allAnswered) {
        showNotification('Por favor, responda todas las preguntas', 'error');
        return;
    }
    
    // Collect form data
    const formData = new FormData(form);
    const data = {};
    
    // Process form data
    formData.forEach((value, key) => {
        if (key.includes('_Score')) {
            data[key] = parseInt(value);
        } else if (key === 'age') {
            data[key] = parseInt(value);
        } else if (key === 'result') {
            // Calculate result based on scores
            let totalScore = 0;
            for (let i = 1; i <= 10; i++) {
                totalScore += parseInt(formData.get(`A${i}_Score`));
            }
            data[key] = totalScore * 1.5 + Math.random() * 2;
        } else {
            data[key] = value;
        }
    });
    
    // Add result field
    if (!data.result) {
        let totalScore = 0;
        for (let i = 1; i <= 10; i++) {
            totalScore += data[`A${i}_Score`];
        }
        data.result = totalScore * 1.5 + Math.random() * 2;
    }
    
    // Show loading
    showLoading();
    
    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error en la predicción');
        }
        
        const result = await response.json();
        
        // Hide loading and show result
        hideLoading();
        showResult(result);
        
    } catch (error) {
        hideLoading();
        console.error('Error:', error);
        showNotification(error.message || 'Error al realizar la predicción. Verifique que la API esté ejecutándose.', 'error');
    }
}

// Show Loading
function showLoading() {
    loadingOverlay.classList.add('active');
    submitBtn.disabled = true;
}

// Hide Loading
function hideLoading() {
    loadingOverlay.classList.remove('active');
    submitBtn.disabled = false;
}

// Show Result
function showResult(result) {
    const { prediction, prediction_label, probability } = result;
    
    // Scroll to result
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    // Set icon
    const resultIcon = document.getElementById('resultIcon');
    if (prediction === 1) {
        resultIcon.innerHTML = '⚠️';
        resultIcon.style.color = 'var(--warning)';
    } else {
        resultIcon.innerHTML = '✅';
        resultIcon.style.color = 'var(--success)';
    }
    
    // Set title and subtitle
    const resultTitle = document.getElementById('resultTitle');
    const resultSubtitle = document.getElementById('resultSubtitle');
    
    if (prediction === 1) {
        resultTitle.textContent = 'Indicadores de ASD Detectados';
        resultTitle.style.color = 'var(--warning)';
        resultSubtitle.textContent = 'Los resultados sugieren la presencia de características asociadas al Trastorno del Espectro Autista.';
    } else {
        resultTitle.textContent = 'No se Detectaron Indicadores de ASD';
        resultTitle.style.color = 'var(--success)';
        resultSubtitle.textContent = 'Los resultados no sugieren la presencia de características asociadas al Trastorno del Espectro Autista.';
    }
    
    // Set probability
    const probabilityValue = document.getElementById('probabilityValue');
    const probabilityFill = document.getElementById('probabilityFill');
    
    const percentage = (probability * 100).toFixed(1);
    probabilityValue.textContent = `${percentage}%`;
    
    // Animate probability bar
    setTimeout(() => {
        probabilityFill.style.width = `${percentage}%`;
    }, 100);
    
    // Show result card
    resultCard.style.display = 'block';
    
    // Hide form
    document.querySelector('.form-card').style.display = 'none';
}

// Hide Result
function hideResult() {
    resultCard.style.display = 'none';
    document.querySelector('.form-card').style.display = 'block';
}

// Handle Reset
function handleReset() {
    // Reset form
    form.reset();
    
    // Reset all toggle buttons
    const toggleBtns = document.querySelectorAll('.toggle-btn');
    toggleBtns.forEach(btn => btn.classList.remove('active'));
    
    // Reset hidden inputs
    const hiddenInputs = document.querySelectorAll('.question-item input[type="hidden"]');
    hiddenInputs.forEach(input => input.value = '');
    
    // Animation
    const formCard = document.querySelector('.form-card');
    formCard.style.animation = 'none';
    setTimeout(() => {
        formCard.style.animation = '';
    }, 10);
    
    showNotification('Formulario limpiado', 'success');
}

// Handle New Evaluation
function handleNewEvaluation() {
    hideResult();
    handleReset();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Show Notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style notification
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '1rem 1.5rem',
        borderRadius: '0.75rem',
        color: 'white',
        fontWeight: '600',
        zIndex: '10000',
        animation: 'slideInRight 0.3s ease',
        boxShadow: '0 10px 30px rgba(0, 0, 0, 0.3)',
        maxWidth: '400px',
        backdropFilter: 'blur(10px)'
    });
    
    // Set background color based on type
    if (type === 'success') {
        notification.style.background = 'linear-gradient(135deg, #10b981, #059669)';
    } else if (type === 'error') {
        notification.style.background = 'linear-gradient(135deg, #ef4444, #dc2626)';
    } else {
        notification.style.background = 'linear-gradient(135deg, #667eea, #764ba2)';
    }
    
    // Add to document
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add animation styles
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Auto-check API status every 30 seconds
setInterval(checkAPIStatus, 30000);

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add input validation
const ageInput = document.getElementById('age');
if (ageInput) {
    ageInput.addEventListener('input', (e) => {
        const value = parseInt(e.target.value);
        if (value < 1) e.target.value = 1;
        if (value > 120) e.target.value = 120;
    });
}

// Form field animations
const formInputs = document.querySelectorAll('input, select');
formInputs.forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'translateY(-2px)';
        this.parentElement.style.transition = 'transform 0.2s ease';
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.style.transform = '';
    });
});

// Console log for debugging
console.log('🚀 ASD Predictor Web App initialized');
console.log('📡 API URL:', API_URL);
console.log('✨ Ready to make predictions!');
