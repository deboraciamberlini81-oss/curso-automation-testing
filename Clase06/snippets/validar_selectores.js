// Clase06 - Validación masiva de selectores CSS

const selectores = [
    '#user-name',
    '#password',
    '#login-button'
];

selectores.forEach(selector => {
    const elementos = document.querySelectorAll(selector);

    console.log(
        selector,
        'Coincidencias:',
        elementos.length,
        elementos.length === 1 ? 'OK' : 'ERROR'
    );
});