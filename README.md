# Proyecto de Automatización QA – Page Object Model (POM)

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con **Python, Selenium WebDriver y Pytest**, aplicando el patrón de diseño **Page Object Model (POM)**.

El objetivo es automatizar los principales flujos de navegación de la aplicación SauceDemo, mejorar la organización del código y facilitar su mantenimiento y reutilización.

## Tecnologías utilizadas

- Python 3.12
- Selenium WebDriver 4.50.0
- Pytest 7.4.4
- Pytest-HTML 4.2.0
- Page Object Model (POM)
- Google Chrome

## Estructura del proyecto

```text
curso-automation_testing/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_catalogo.py
│   ├── test_carrito.py
│   └── test_calculadora.py
│
├── Clase05/
├── Clase06/
├── Clase07/
├── calculadora/
│
├── pytest.ini
├── preentrega_pom.html
└── README.md
```

## Patrón Page Object Model

Se implementó POM para separar los localizadores y las acciones de cada página de los casos de prueba.

- **LoginPage:** apertura de la aplicación e inicio de sesión.
- **InventoryPage:** consulta del catálogo, productos, precios y carrito.
- **CartPage:** consulta y validación de productos agregados al carrito.

## Casos de prueba automatizados

| Archivo | Validación |
|---|---|
| `test_login.py` | Inicio de sesión exitoso |
| `test_catalogo.py` | Visualización del catálogo y productos |
| `test_carrito.py` | Agregado y verificación de productos en el carrito |

## Fixture de WebDriver

Se configuró una fixture llamada `driver` en `tests/conftest.py`, responsable de:

1. Inicializar Google Chrome.
2. Maximizar la ventana.
3. Proporcionar el navegador a los casos de prueba.
4. Cerrar el navegador al finalizar cada prueba.

## Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest -v
```

Ejecutar solamente las pruebas POM:

```bash
python -m pytest -m pom -v
```

Ejecutar las pruebas Smoke:

```bash
python -m pytest -m smoke -v
```

Generar el reporte HTML solicitado:

```bash
python -m pytest -m smoke --html=preentrega_pom.html --self-contained-html
```

## Reporte de ejecución

El proyecto genera un reporte HTML con el detalle de los resultados de ejecución.

Archivo: `preentrega_pom.html`

Última ejecución de Smoke:

- 7 pruebas aprobadas.
- 8 pruebas deseleccionadas.

Pruebas POM:

- 3 pruebas aprobadas.

## Conclusión

La implementación del patrón Page Object Model permite mejorar la legibilidad, organización y mantenibilidad de las pruebas automatizadas.

Este proyecto forma parte del proceso de aprendizaje y desarrollo de habilidades en **QA Automation**, utilizando herramientas y buenas prácticas de automatización de pruebas.