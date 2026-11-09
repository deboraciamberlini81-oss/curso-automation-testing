# QA Automation Framework – Python, Selenium & API Testing

## Descripción

Proyecto de automatización de pruebas desarrollado con **Python, Selenium WebDriver, Pytest y Requests**, aplicando buenas prácticas de QA Automation.

El framework integra pruebas funcionales de interfaz de usuario (UI Testing) y pruebas de servicios REST (API Testing), utilizando el patrón de diseño **Page Object Model (POM)**, parametrización y lectura de datos externos mediante archivos CSV y JSON.

El objetivo es validar los principales flujos de una aplicación web, verificar respuestas de servicios API y desarrollar una estructura organizada, reutilizable y escalable.

## Tecnologías utilizadas

- Python 3.12
- Selenium WebDriver 4.50.0
- Pytest 7.4.4
- Pytest-HTML 4.2.0
- Requests 2.32.2
- Page Object Model (POM)
- Data-Driven Testing
- Parametrización con Pytest
- Lectura de archivos CSV y JSON
- API Testing (GET y POST)
- Google Chrome
- Git y GitHub

## Estructura del proyecto

```text
curso-automation_testing/
│
├── datos/
│   ├── login.csv
│   ├── productos.json
│   └── login_api.json
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_calculadora.py
│   ├── test_login_csv.py
│   ├── test_catalogo.py
│   └── test_carrito_json.py
│
├── tests_api/
│   ├── test_login_api.py
│   ├── test_users_api.py
│   └── test_create_user_api.py
│
├── utils/
│   └── lectura_datos.py
│
├── Clase05/
├── Clase06/
├── Clase07/
├── calculadora/
├── assets/
│
├── pytest.ini
├── README.md
└── .gitignore
```

## 1. Automatización UI – Selenium WebDriver

Se implementaron pruebas funcionales sobre la aplicación SauceDemo.

### Page Object Model (POM)

Se utilizó el patrón POM para separar las acciones y localizadores de cada página de los casos de prueba.

- **LoginPage:** apertura de la aplicación, inicio de sesión y lectura de mensajes de error.
- **InventoryPage:** consulta del catálogo, productos, precios y agregado de productos al carrito.
- **CartPage:** consulta y validación de los productos agregados.

### Fixture de WebDriver

Se configuró una fixture `driver` en `tests/conftest.py`, responsable de:

1. Inicializar Google Chrome.
2. Maximizar la ventana.
3. Proporcionar el navegador a los casos de prueba.
4. Cerrar el navegador al finalizar cada prueba.

## 2. Data-Driven Testing – Datos externos

Se creó el módulo `utils/lectura_datos.py` para centralizar la lectura de archivos CSV y JSON.

### Archivo CSV: login.csv

Contiene diferentes combinaciones de usuarios y contraseñas para validar:

- Inicio de sesión exitoso.
- Usuario bloqueado.
- Credenciales incorrectas.
- Usuario inexistente.

### Archivo JSON: productos.json

Contiene los nombres de los productos y sus XPath correspondientes para automatizar su agregado al carrito.

### Parametrización

Se utilizó `@pytest.mark.parametrize` para ejecutar múltiples escenarios con diferentes conjuntos de datos, evitando duplicar código.

## 3. API Testing – Requests

Se incorporó una suite independiente en `tests_api/` para validar servicios REST utilizando la librería Requests.

### Login API – POST

Endpoint:

`https://reqres.in/api/login`

Escenarios implementados:

| Escenario | Resultado esperado |
|---|---|
| Login con credenciales válidas | HTTP 200 + token |
| Login sin contraseña | HTTP 400 + error |

Los escenarios se cargan desde `datos/login_api.json` y se ejecutan mediante parametrización con Pytest.

### Users API – GET

Endpoint:

`https://reqres.in/api/users?page=1`

Validaciones realizadas:

- Código de respuesta HTTP 200.
- Existencia de la lista de usuarios.
- Presencia de los campos `id`, `email`, `first_name` y `last_name`.
- Validación adicional: los avatares deben finalizar en `.jpg`.

### Create User API – POST

Endpoint:

`https://reqres.in/api/users`

Se implementaron pruebas parametrizadas para crear usuarios con distintos nombres y trabajos.

Validaciones realizadas:

- Código de respuesta HTTP 201 (Created).
- Coincidencia del nombre enviado con el devuelto por la API.
- Coincidencia del trabajo enviado con el devuelto por la API.
- Existencia de un identificador (`id`).
- Existencia del campo `createdAt`.
- Verificación de que `createdAt` contenga el año actual.

Se utilizaron datos fijos parametrizados mediante `@pytest.mark.parametrize`.

## 4. Marcadores de Pytest

Se configuraron marcadores para organizar la ejecución de las pruebas:

| Marcador | Descripción |
|---|---|
| `smoke` | Pruebas principales de la aplicación |
| `pom` | Pruebas con Page Object Model |
| `exception` | Manejo de excepciones |
| `api` | Pruebas de servicios REST |

## 5. Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest -v
```

Ejecutar solamente las pruebas API:

```bash
python -m pytest -m api -v
```

Ejecutar solamente las pruebas UI con POM:

```bash
python -m pytest -m pom -v
```

Ejecutar las pruebas Smoke:

```bash
python -m pytest -m smoke -v
```

Ejecutar la suite completa de UI + API:

```bash
python -m pytest tests/ tests_api/ -v
```

Generar un reporte HTML combinado:

```bash
python -m pytest tests/ tests_api/ --html=reporte_completo.html --self-contained-html
```

## 6. Resultados de ejecución

Última ejecución completa del framework:

**30 pruebas aprobadas – 0 fallidas.**

| Suite | Pruebas aprobadas |
|---|---:|
| Calculadora | 12 |
| Selenium / UI | 12 |
| API Testing | 6 |
| **Total** | **30** |

Tiempo de ejecución de la última suite completa: 60.55 segundos.

### Ejecución independiente de API Testing

- 6 pruebas aprobadas.
- 0 pruebas fallidas.

### Reporte HTML

Se generó el reporte combinado:

`reporte_completo.html`

El informe permite consultar los resultados de las pruebas de interfaz y API en un único archivo.

## 7. Control de versiones

El proyecto utiliza Git y GitHub para el control de versiones.

Se trabaja mediante ramas de funcionalidades para organizar los cambios y mantener un historial de desarrollo.

Repositorio:

[curso-automation-testing](https://github.com/deboraciamberlini81-oss/curso-automation-testing)

## Conclusión

Este proyecto representa la integración de diferentes técnicas de automatización de pruebas:

- Automatización funcional de interfaces web.
- Diseño con Page Object Model.
- Pruebas basadas en datos externos.
- Parametrización de escenarios.
- Validación de servicios REST mediante métodos GET y POST.
- Pruebas de creación de usuarios y validación de respuestas HTTP.
- Organización y ejecución de suites con Pytest.
- Generación de reportes HTML.
- Control de versiones con Git y GitHub.

El framework constituye una base de aprendizaje y práctica profesional en **QA Automation**, con una estructura preparada para incorporar nuevas funcionalidades, validaciones y escenarios de prueba.