# Clase06 - Selectores robustos con CSS y XPath

## 1. Descripción del proyecto

Ejercicio práctico de Automation Testing de Talento Lab, enfocado en la identificación y validación de selectores robustos para futuras pruebas automatizadas con Selenium WebDriver.

Se utilizó el formulario de inicio de sesión de SauceDemo para localizar elementos HTML sin depender de su posición ni de su diseño visual.

## 2. Objetivos

- Identificar elementos mediante Chrome DevTools.
- Obtener selectores CSS y XPath relativos.
- Priorizar identificadores únicos.
- Validar selectores desde la consola del navegador.
- Ejecutar una comprobación masiva.
- Documentar las decisiones técnicas.

## 3. Sitio de pruebas

- Nombre: SauceDemo.
- URL: https://www.saucedemo.com/
- Navegador: Google Chrome.
- Herramienta: Chrome DevTools.

## 4. Elementos evaluados

| Elemento | ID |
|---|---|
| Usuario | `user-name` |
| Contraseña | `password` |
| Botón Login | `login-button` |

## 5. Selectores utilizados

- Usuario: `#user-name`
- Contraseña: `#password`
- Botón Login: `#login-button`

También se construyeron sus correspondientes XPath relativos.

## 6. Validaciones realizadas

- Inspección de elementos HTML.
- Validación de selectores CSS mediante `document.querySelector()`.
- Validación de XPath mediante `$x()`.
- Comprobación masiva de coincidencias.
- Prueba visual mediante cambios temporales de estilos.

## 7. Resultado

Los tres selectores CSS y los tres XPath localizaron correctamente sus respectivos elementos.

La prueba masiva confirmó una única coincidencia para cada selector CSS.

## 8. Estructura del proyecto

```text
Clase06/
│
├── README.md
└── selectores-talento.md
```

## 9. Conclusión

La actividad permitió aplicar buenas prácticas de selección de elementos HTML, priorizando atributos estables e identificadores únicos.

La documentación servirá como referencia para futuras automatizaciones con Selenium WebDriver y contribuirá a reducir errores cuando se realicen modificaciones en el diseño de la aplicación.