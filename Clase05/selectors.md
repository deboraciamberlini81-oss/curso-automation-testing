
# Documentación de selectores CSS - Calculadora

## 1. Objetivo

Documentar los selectores CSS de los elementos HTML de la calculadora web para facilitar su futura automatización con Selenium WebDriver.

## 2. Tabla de selectores

| Elemento | ID | Name | Selector CSS | Descripción |
|---|---|---|---|---|
| Formulario | form-calculadora | form-calculadora | `#form-calculadora` | Formulario principal |
| Primer número | num1 | primer_numero | `#num1` | Campo del primer número |
| Operación | operacion | operacion | `#operacion` | Selector de operación matemática |
| Segundo número | num2 | segundo_numero | `#num2` | Campo del segundo número |
| Resultado | resultado | resultado | `#resultado` | Campo de resultado |
| Botón calcular | btn-calcular | btn_calcular | `#btn-calcular` | Botón para ejecutar el cálculo |
| Botón limpiar | btn-limpiar | btn_limpiar | `#btn-limpiar` | Botón para limpiar los campos |

## 3. Selectores adicionales

| Elemento | Selector CSS | Uso |
|---|---|---|
| Tarjeta calculadora | `.calculadora` | Localizar el contenedor |
| Encabezado | `.calculadora__encabezado` | Localizar el encabezado |
| Descripción | `.calculadora__descripcion` | Localizar el texto descriptivo |
| Campos | `.campo` | Identificar los grupos de campos |
| Inputs | `.campo__input` | Localizar campos de entrada |
| Botón principal | `.boton--principal` | Identificar el botón Calcular |
| Botón secundario | `.boton--secundario` | Identificar el botón Limpiar |

## 4. Ejemplos para Selenium

```python
from selenium.webdriver.common.by import By

# Localizar el primer número
driver.find_element(By.ID, "num1")

# Localizar el segundo número
driver.find_element(By.ID, "num2")

# Localizar la operación
driver.find_element(By.CSS_SELECTOR, "#operacion")

# Localizar el botón calcular
driver.find_element(By.CSS_SELECTOR, "#btn-calcular")

# Localizar el botón limpiar
driver.find_element(By.ID, "btn-limpiar")
```

## 5. Verificaciones QA

- Cada elemento interactivo tiene un identificador único.
- Los atributos ID no se repiten.
- Los atributos NAME no se repiten.
- Los campos tienen etiquetas LABEL asociadas.
- Los selectores CSS apuntan a elementos específicos.
- Los selectores están preparados para futuras pruebas con Selenium.

## 6. Observaciones

La interfaz es estática y no contiene JavaScript.

Los selectores documentados servirán como referencia para desarrollar los futuros casos de prueba automatizados con Selenium WebDriver.
