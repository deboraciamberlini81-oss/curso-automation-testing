
# Clase05 - Calculadora Web

## 1. Descripción del proyecto

Desarrollo de una interfaz web estática para una calculadora matemática, como parte de las actividades prácticas de Automation Testing de Talento Lab.

El objetivo es preparar una estructura HTML y CSS organizada, con identificadores únicos y selectores estables para su futura automatización con Selenium WebDriver.

## 2. Estructura del proyecto

```text
Clase05/
│
├── index.html
├── estilos.css
├── selectors.md
└── README.md
```

## 3. Tecnologías utilizadas

- HTML5
- CSS3
- Google Chrome
- Chrome DevTools
- Selenium WebDriver (para futura automatización)

## 4. Cómo ejecutar el proyecto

1. Abrir la carpeta `Clase05`.
2. Localizar el archivo `index.html`.
3. Abrirlo con Google Chrome.
4. Verificar que la calculadora se visualice correctamente.

No requiere servidor ni instalación de dependencias.

## 5. Verificación con DevTools

1. Abrir la calculadora en Chrome.
2. Presionar `F12` para abrir las herramientas de desarrollador.
3. Seleccionar la pestaña `Elements`.
4. Inspeccionar los campos y botones.
5. Comprobar que cada elemento interactivo tenga un ID único.

## 6. Prueba rápida de selectores CSS

En la pestaña `Console`, ejecutar:

```javascript
document.querySelector('#num1').style.border = '2px solid red';
```

Si el borde del primer campo cambia a rojo, el selector funciona correctamente.

Otros selectores que se pueden comprobar:

```javascript
document.querySelector('#num2').style.border = '2px solid red';

document.querySelector('#operacion').style.border = '2px solid red';

document.querySelector('#btn-calcular').style.outline = '2px solid red';

document.querySelector('#btn-limpiar').style.outline = '2px solid red';
```

## 7. Documentación de selectores

El archivo `selectors.md` contiene:

- Identificadores HTML.
- Atributos name.
- Selectores CSS.
- Descripción de cada elemento.
- Ejemplos de localización con Selenium.

## 8. Alcance del proyecto

La calculadora contiene una interfaz estática.

No incluye JavaScript ni lógica de operaciones matemáticas, ya que el objetivo de esta actividad es preparar el frontend para futuras pruebas automatizadas.

## 9. Conclusión

Se construyó una interfaz web organizada y preparada para automatización, aplicando buenas prácticas de identificación de elementos HTML y documentación de selectores CSS.
