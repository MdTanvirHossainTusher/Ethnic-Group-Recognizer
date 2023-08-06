// Get all card elements
const cards = document.querySelectorAll('.card');

// Get the popup elements
const overlay = document.querySelector('.overlay');
const popup = document.querySelector('.popup');
const popupContent = document.querySelector('.popup-content');
const closeBtn = document.querySelector('.close');

// Event listeners for each card to show the popup on click
cards.forEach(card => {
    card.addEventListener('click', () => {
        const title = card.querySelector('h3').textContent;
        const description = card.querySelector('.card-popup p').textContent;
        popupContent.innerHTML = `
            <h3>${title}</h3>
            <p>${description}</p>
        `;
        overlay.style.display = 'block';
        popup.style.display = 'block';
    });
});

// Event listener for close button to hide the popup
closeBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
});
