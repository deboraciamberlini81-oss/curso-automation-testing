# Clase06 - Selectores robustos con Selenium

## 1. Descripción del ejercicio

Actividad práctica de Automation Testing de Talento Lab.

El objetivo es identificar, seleccionar y validar elementos HTML mediante selectores CSS y XPath relativos, priorizando identificadores únicos y atributos estables que no dependan de la estructura visual de la página.

## 2. Sitio utilizado

- Aplicación: SauceDemo
- URL: https://www.saucedemo.com/
- Herramienta de inspección: Google Chrome DevTools
- Pestañas utilizadas: Elements y Console

## 3. Tabla de selectores

| Elemento | Selector CSS | XPath relativo | Resultado |
|---|---|---|---|
| Usuario | `#user-name` | `//*[@id='user-name']` | Validado |
| Contraseña | `#password` | `//*[@id='password']` | Validado |
| Botón Login | `#login-button` | `//*[@id='login-button']` | Validado |

## 4. Justificación de los selectores

### Usuario
- CSS: `#user-name`
- XPath: `//*[@id='user-name']`

Se seleccionó el ID porque identifica directamente el campo de usuario y no depende de su posición en el formulario ni de las clases visuales.

### Contraseña
- CSS: `#password`
- XPath: `//*[@id='password']`

Se eligió el ID porque es específico y permite localizar el campo de contraseña de forma directa.

### Botón Login
- CSS: `#login-button`
- XPath: `//*[@id='login-button']`

Se utilizó el ID porque identifica exclusivamente el botón de inicio de sesión y evita depender de su ubicación o diseño.

## 5. Validación de selectores CSS

Se utilizó `document.querySelector()` para comprobar que los selectores localizaran los elementos correctos.

Ejemplo:

```javascript
document.querySelector('#user-name');
document.querySelector('#password');
document.querySelector('#login-button');
```

## 6. Validación de XPath

Se utilizó `$x()` desde Chrome DevTools para comprobar los XPath relativos.

```javascript
$x("//*[@id='user-name']");
$x("//*[@id='password']");
$x("//*[@id='login-button']");
```

Los tres XPath localizaron correctamente sus respectivos elementos.

## 7. Test masivo de selectores CSS

Se ejecutó el siguiente snippet para comprobar la cantidad de coincidencias de cada selector:

```javascript
const selectores = [
    '#user-name',
    '#password',
    '#login-button'
];

selectores.forEach(selector => {
    const elemento = document.querySelectorAll(selector);

    console.log(
        selector,
        'Coincidencias:',
        elemento.length,
        elemento.length === 1 ? 'OK' : 'ERROR'
    );
});
```

### Resultado obtenido

Los tres selectores devolvieron una coincidencia cada uno.

- `#user-name`: 1 coincidencia.
- `#password`: 1 coincidencia.
- `#login-button`: 1 coincidencia.

## 8. Prueba visual de selectores

Se realizó una prueba visual mediante JavaScript para modificar temporalmente los estilos de los elementos.

```javascript
['#user-name', '#password', '#login-button'].forEach(selector => {
    const elemento = document.querySelector(selector);

    elemento.style.outline = '3px solid lime';
    elemento.style.outlineOffset = '3px';
});
```

Los contornos permitieron identificar visualmente los elementos seleccionados.

Nota: SauceDemo mantiene estilos propios en los campos de entrada, por lo que el cambio de color de fondo no se visualizó como se esperaba. La validación de los selectores sí fue satisfactoria.

## 9. Buenas prácticas aplicadas

- Priorizar identificadores únicos.
- Utilizar selectores CSS simples y específicos.
- Utilizar XPath relativos.
- Evitar rutas XPath absolutas.
- Evitar selectores basados en posiciones.
- No depender de clases relacionadas con el diseño visual.
- Comprobar que cada selector encuentre un único elemento.
- Documentar la justificación de cada selector.

## 10. Conclusión

Se identificaron y validaron tres elementos principales del formulario de inicio de sesión de SauceDemo mediante CSS y XPath.

Los resultados demostraron que los selectores elegidos localizan correctamente los elementos y no dependen de la distribución visual del formulario.

La documentación queda preparada como referencia para futuras pruebas automatizadas con Selenium WebDriver.