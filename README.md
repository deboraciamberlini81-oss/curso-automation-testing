# Proyecto de Automatización QA – Page Object Model (POM)

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con **Python, Selenium WebDriver y Pytest**, aplicando el patrón de diseño **Page Object Model (POM)** y la lectura de datos externos mediante archivos CSV y JSON.

El objetivo es automatizar los principales flujos de navegación de la aplicación SauceDemo, mejorar la organización del código y facilitar el mantenimiento, la reutilización y la ampliación de los casos de prueba.

## Tecnologías utilizadas

- Python 3.12
- Selenium WebDriver 4.50.0
- Pytest 7.4.4
- Pytest-HTML 4.2.0
- Page Object Model (POM)
- Parametrización con Pytest
- Lectura de archivos CSV y JSON
- Google Chrome

## Estructura del proyecto

```text
curso-automation_testing/
│
├── datos/
│   ├── login.csv
│   └── productos.json
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
├── utils/
│   └── lectura_datos.py
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

## Patrón Page Object Model (POM)

Se implementó POM para separar los localizadores y las acciones de cada página de los casos de prueba.

- **LoginPage:** apertura de la aplicación, inicio de sesión y lectura de mensajes de error.
- **InventoryPage:** consulta del catálogo, productos, precios y agregado de productos al carrito.
- **CartPage:** consulta y validación de los productos agregados al carrito.

## Lectura de datos externos

Se creó el módulo `utils/lectura_datos.py` para centralizar la lectura de archivos externos.

### Archivo CSV: login.csv

Contiene diferentes combinaciones de usuarios y contraseñas para validar:

- Inicio de sesión exitoso.
- Usuario bloqueado.
- Credenciales incorrectas.
- Usuario inexistente.

### Archivo JSON: productos.json

Contiene los nombres de los productos y sus XPath correspondientes para automatizar su agregado al carrito.

## Parametrización de pruebas

Se utilizó `@pytest.mark.parametrize` para ejecutar los casos de prueba con diferentes conjuntos de datos sin duplicar código.

| Archivo | Datos externos | Casos ejecutados |
|---|---|---:|
| `test_login.py` | `login.csv` | 6 |
| `test_carrito.py` | `productos.json` | 4 |
| `test_catalogo.py` | — | 1 |
| **Total POM** | | **11** |

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

Generar el reporte HTML:

```bash
python -m pytest -m smoke --html=preentrega_pom.html --self-contained-html
```

## Resultados de ejecución

Última validación del módulo POM:

- 11 pruebas aprobadas.
- 12 pruebas deseleccionadas.
- 0 pruebas fallidas.

Validación de los datos externos:

- 6 casos de inicio de sesión ejecutados desde CSV.
- 4 casos de agregado de productos ejecutados desde JSON.

## Conclusión

La implementación de Page Object Model, junto con la lectura de datos externos y la parametrización de Pytest, permite desarrollar pruebas automatizadas más organizadas, reutilizables y fáciles de mantener.

Este proyecto forma parte del proceso de aprendizaje y desarrollo de habilidades en **QA Automation**, aplicando buenas prácticas de automatización de pruebas funcionales.
