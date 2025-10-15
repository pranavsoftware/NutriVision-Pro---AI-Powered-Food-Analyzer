// Dashboard JavaScript Functionality

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeDashboard();
});

// Initialize dashboard functionality
function initializeDashboard() {
    // Add loading animations
    addLoadingAnimations();
    
    // Initialize feature cards
    initializeFeatureCards();
    
    // Add scroll animations
    addScrollAnimations();
    
    // Initialize floating elements
    initializeFloatingElements();
    
    // Add performance optimizations
    optimizePerformance();
}

// Add loading animations to elements
function addLoadingAnimations() {
    const animatedElements = document.querySelectorAll('.hero-section, .features-grid, .info-section');
    
    animatedElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            element.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200);
    });
}

// Initialize feature card interactions
function initializeFeatureCards() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    featureCards.forEach(card => {
        // Add hover sound effect (optional)
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px) scale(1.02)';
            
            // Add ripple effect
            createRippleEffect(card);
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1)';
        });
        
        // Add click animation
        card.addEventListener('click', (e) => {
            if (!e.target.closest('.card-button')) {
                createClickAnimation(card);
            }
        });
    });
}

// Create ripple effect on card hover
function createRippleEffect(card) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple-effect';
    ripple.style.cssText = `
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.3), transparent 70%);
        transform: translate(-50%, -50%);
        animation: ripple 1s ease-out;
        pointer-events: none;
        z-index: 1;
    `;
    
    card.style.position = 'relative';
    card.appendChild(ripple);
    
    // Add ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                width: 200px;
                height: 200px;
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    setTimeout(() => {
        ripple.remove();
    }, 1000);
}

// Create click animation
function createClickAnimation(element) {
    element.style.transform = 'scale(0.95)';
    
    setTimeout(() => {
        element.style.transform = 'translateY(-10px) scale(1.02)';
    }, 150);
}

// Navigation function for feature buttons
function navigateToFeature(feature) {
    // Add click animation
    const button = event.target.closest('.card-button');
    if (button) {
        button.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
            button.style.transform = 'translateY(-2px) scale(1)';
        }, 100);
    }
    
    // Show loading state
    showFeatureLoading(feature);
    
    // Navigate based on feature type
    setTimeout(() => {
        switch(feature) {
            case 'scan':
                // Navigate to food scanning page
                window.location.href = '/dashboard';  // Navigate to dashboard
                break;
            case 'meal':
                // Navigate to meal planner
                alert('🍽️ Meal Planner feature coming soon!\n\nThis will help you create personalized meal plans.');
                break;
            case 'query':
                // Navigate to query page
                alert('💬 Ask Query feature coming soon!\n\nChat with our AI nutrition assistant.');
                break;
            case 'expert':
                // Navigate to diet expert
                alert('👨‍⚕️ Diet Expert feature coming soon!\n\nGet professional dietary advice.');
                break;
            default:
                console.log('Unknown feature:', feature);
        }
    }, 1000);
}

// Show loading state for feature
function showFeatureLoading(feature) {
    const featureCard = document.querySelector(`[data-feature="${feature}"]`);
    const button = featureCard.querySelector('.card-button');
    const originalText = button.innerHTML;
    
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    button.style.opacity = '0.7';
    button.style.pointerEvents = 'none';
    
    setTimeout(() => {
        button.innerHTML = originalText;
        button.style.opacity = '1';
        button.style.pointerEvents = 'auto';
    }, 1000);
}

// Add scroll animations
function addScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                
                // Add staggered animation for grid items
                if (entry.target.classList.contains('features-grid')) {
                    const cards = entry.target.querySelectorAll('.feature-card');
                    cards.forEach((card, index) => {
                        setTimeout(() => {
                            card.style.animation = `slideInUp 0.6s ease-out ${index * 0.1}s both`;
                        }, 100);
                    });
                }
            }
        });
    }, observerOptions);
    
    // Observe elements for scroll animations
    const observeElements = document.querySelectorAll('.features-section, .info-section');
    observeElements.forEach(el => observer.observe(el));
    
    // Add slide-in-up animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
}

// Initialize floating elements
function initializeFloatingElements() {
    const floatingElements = document.querySelectorAll('.floating-emoji');
    
    floatingElements.forEach((element, index) => {
        // Add random movement
        setInterval(() => {
            const randomX = Math.random() * 20 - 10; // -10 to +10
            const randomY = Math.random() * 20 - 10; // -10 to +10
            
            element.style.transform = `translate(${randomX}px, ${randomY}px)`;
        }, 3000 + index * 500);
    });
}

// Performance optimizations
function optimizePerformance() {
    // Debounce scroll events
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        
        scrollTimeout = setTimeout(() => {
            // Update scroll-based animations
            updateScrollAnimations();
        }, 16); // ~60fps
    });
    
    // Preload images and resources
    preloadResources();
    
    // Add will-change properties for better performance
    const animatedElements = document.querySelectorAll('.feature-card, .floating-emoji, .stat-emoji');
    animatedElements.forEach(el => {
        el.style.willChange = 'transform';
    });
}

// Update scroll-based animations
function updateScrollAnimations() {
    const scrollY = window.scrollY;
    const windowHeight = window.innerHeight;
    
    // Parallax effect for floating elements
    const floatingElements = document.querySelectorAll('.floating-emoji');
    floatingElements.forEach((element, index) => {
        const speed = 0.5 + index * 0.1;
        const yPos = -(scrollY * speed);
        element.style.transform = `translateY(${yPos}px)`;
    });
}

// Preload resources for better performance
function preloadResources() {
    // Preload fonts
    const fontLink = document.createElement('link');
    fontLink.rel = 'preload';
    fontLink.href = 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap';
    fontLink.as = 'style';
    document.head.appendChild(fontLink);
    
    // Preload Font Awesome
    const faLink = document.createElement('link');
    faLink.rel = 'preload';
    faLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
    faLink.as = 'style';
    document.head.appendChild(faLink);
}

// Utility function to create smooth transitions
function smoothTransition(element, properties, duration = 300) {
    return new Promise(resolve => {
        element.style.transition = `all ${duration}ms cubic-bezier(0.4, 0, 0.2, 1)`;
        
        Object.keys(properties).forEach(property => {
            element.style[property] = properties[property];
        });
        
        setTimeout(resolve, duration);
    });
}

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    const featureCards = document.querySelectorAll('.feature-card');
    const currentFocus = document.activeElement;
    
    if (e.key === 'Tab') {
        // Enhanced tab navigation
        if (currentFocus.classList.contains('card-button')) {
            currentFocus.closest('.feature-card').style.outline = '2px solid var(--primary-color)';
        }
    }
    
    if (e.key === 'Enter' && currentFocus.classList.contains('card-button')) {
        currentFocus.click();
    }
});

// Initialize accessibility features
function initializeAccessibility() {
    // Add ARIA labels
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        const title = card.querySelector('.card-title').textContent;
        card.setAttribute('role', 'button');
        card.setAttribute('aria-label', `Navigate to ${title} feature`);
        card.setAttribute('tabindex', '0');
    });
    
    // Add skip navigation
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'skip-link';
    skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: var(--primary-color);
        color: white;
        padding: 8px;
        text-decoration: none;
        border-radius: 4px;
        z-index: 1000;
    `;
    
    skipLink.addEventListener('focus', () => {
        skipLink.style.top = '6px';
    });
    
    skipLink.addEventListener('blur', () => {
        skipLink.style.top = '-40px';
    });
    
    document.body.insertBefore(skipLink, document.body.firstChild);
}

// Initialize accessibility when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeAccessibility);

// Export functions for external use
window.DashboardAPI = {
    navigateToFeature,
    smoothTransition,
    createRippleEffect
};
