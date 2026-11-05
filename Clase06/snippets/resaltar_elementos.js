// Clase06 - Resaltar elementos del formulario SauceDemo

const selectores = [
    '#user-name',
    '#password',
    '#login-button'
];

selectores.forEach(selector => {
    const elemento = document.querySelector(selector);

    if (elemento) {
        elemento.style.outline = '3px solid lime';
        elemento.style.outlineOffset = '3px';

        console.log(selector, 'Elemento resaltado correctamente');
    } else {
        console.error(selector, 'No se encontró el elemento');
    }
});