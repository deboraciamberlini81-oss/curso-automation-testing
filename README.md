# QA Automation Framework – Python, Selenium & API Testing

![CI TalentoLab](https://github.com/deboraciamberlini81-oss/curso-automation-testing/actions/workflows/ci.yml/badge.svg)

**Proyecto de automatización de pruebas QA** que integra pruebas funcionales UI, API Testing y BDD, utilizando Python, Selenium WebDriver, Pytest, Requests y Behave.

## Descripción

Framework de automatización desarrollado como proyecto de aprendizaje y práctica profesional de QA Automation.

El proyecto integra:

- Automatización funcional de interfaces web.
- Diseño Page Object Model (POM).
- Data-Driven Testing mediante archivos CSV y JSON.
- Parametrización de pruebas con Pytest.
- Validación de servicios REST.
- Pruebas End-to-End de ciclo de vida API.
- BDD con Behave y Gherkin.
- Generación de reportes HTML.
- Integración continua mediante GitHub Actions.

## Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| Python 3.12 | Lenguaje de programación |
| Selenium WebDriver 4.50.0 | Automatización UI |
| Pytest 7.4.4 | Framework de pruebas |
| Pytest-HTML 4.2.0 | Reportes HTML |
| Requests | API Testing |
| Behave 1.3.3 | BDD |
| Gherkin | Descripción de escenarios |
| Faker | Generación de datos dinámicos |
| Google Chrome | Navegador de pruebas |
| Git y GitHub | Control de versiones |
| GitHub Actions | Integración continua |

## Estructura del proyecto

```text
curso-automation_testing/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── datos/
│   ├── login.csv
│   ├── login_api.json
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
│   ├── test_calculadora.py
│   ├── test_login_csv.py
│   ├── test_catalogo.py
│   └── test_carrito_json.py
│
├── tests_api/
│   ├── test_login_api.py
│   ├── test_users_api.py
│   ├── test_create_user_api.py
│   └── test_post_lifecycle.py
│
├── tests_behave/
│   └── test_behave_suite.py
│
├── features/
│   ├── login.feature
│   ├── cart.feature
│   ├── environment.py
│   └── steps/
│       ├── login_steps.py
│       └── cart_steps.py
│
├── utils/
│   └── lectura_datos.py
│
├── reports/
├── logs/
├── assets/
├── calculadora/
├── Clase05/
├── Clase06/
├── Clase07/
│
├── behave.ini
├── pytest.ini
├── requirements.txt
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

Se implementó el módulo `utils/lectura_datos.py` para centralizar la lectura de archivos CSV y JSON.

### Archivo CSV: login.csv

Contiene diferentes combinaciones de usuarios y contraseñas para validar:

- Inicio de sesión exitoso.
- Usuario bloqueado.
- Credenciales incorrectas.
- Usuario inexistente.

### Archivo JSON: productos.json

Contiene información de productos y sus localizadores para automatizar su agregado al carrito.

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
| Login con credenciales válidas | HTTP 200 y token |
| Login sin contraseña | HTTP 400 y error |

Los escenarios utilizan datos externos de `datos/login_api.json` y parametrización con Pytest.

### Users API – GET

Endpoint:

`https://reqres.in/api/users?page=1`

Validaciones realizadas:

- Código HTTP 200.
- Existencia de la lista de usuarios.
- Presencia de los campos `id`, `email`, `first_name` y `last_name`.
- Validación de que los avatares finalicen en `.jpg`.

### Create User API – POST

Endpoint:

`https://reqres.in/api/users`

Se implementaron pruebas parametrizadas para crear usuarios con distintos nombres y trabajos.

Validaciones:

- Código HTTP 201 (Created).
- Coincidencia del nombre enviado con el devuelto.
- Coincidencia del trabajo enviado con el devuelto.
- Existencia de un identificador (`id`).
- Existencia del campo `createdAt`.
- Validación del año de creación.

## 4. QA-132 – Ciclo de vida de un recurso API

Se implementó una prueba End-to-End (E2E) utilizando JSONPlaceholder.

### Operaciones verificadas

1. **POST:** creación de un recurso mediante datos dinámicos generados con Faker.
2. **PATCH:** actualización del título del recurso.
3. **DELETE:** eliminación simulada y validación del código HTTP 200.

### Validaciones implementadas

- Códigos de respuesta HTTP.
- Estructura de datos JSON.
- Tipos de datos y contenido de campos.
- Identificación mediante ID.
- Tiempo de respuesta.
- Marcador personalizado `@pytest.mark.e2e`.

**Nota:** JSONPlaceholder simula las operaciones de escritura. Los cambios no se almacenan de forma persistente.

## 5. BDD Testing – Behave y Gherkin (QA-158)

Se incorporó una suite BDD (Behavior Driven Development) utilizando Behave y Gherkin para describir escenarios funcionales en un lenguaje claro.

### Features implementadas

**Login (`features/login.feature`)**

- Login exitoso con `standard_user`.
- Login fallido con usuario inválido.
- Login fallido con usuario bloqueado.
- Login con campos vacíos.

**Carrito (`features/cart.feature`)**

- Inicio de sesión mediante Background.
- Agregar Sauce Labs Backpack al carrito.
- Verificar el contador de productos.
- Comprobar que el producto aparece en el carrito.

### Estructura BDD

- `features/login.feature`
- `features/cart.feature`
- `features/environment.py`
- `features/steps/login_steps.py`
- `features/steps/cart_steps.py`

### Configuración

Se utiliza `behave.ini` para configurar:

- Directorio de features.
- Idioma Gherkin.
- Etiquetas predeterminadas.
- Formatter HTML mediante `behave-html-formatter`.

### Ejecución

Ejecutar todos los escenarios:

```bash
python -m behave
```

Ejecutar solamente Smoke:

```bash
python -m behave --tags=@smoke
```

Ejecutar regresión:

```bash
python -m behave --tags=@regression
```

Generar reporte HTML:

```bash
python -m behave --format html --outfile reports/reporte_behave.html
```

La ejecución verificada registró:

- 2 features aprobadas.
- 5 escenarios aprobados.
- 18 steps aprobados.
- 0 fallos.

El reporte generado se almacena en `reports/reporte_behave.html`.

## 6. Marcadores de Pytest

Se configuraron marcadores personalizados para organizar las pruebas:

| Marcador | Descripción |
|---|---|
| `smoke` | Pruebas principales de la aplicación |
| `pom` | Automatización con Page Object Model |
| `exception` | Manejo de excepciones |
| `api` | Pruebas de servicios REST |
| `e2e` | Pruebas End-to-End de API |
| `bdd` | Pruebas BDD ejecutadas mediante Behave |
| `regression` | Pruebas de regresión funcional |

## 7. Ejecución de pruebas

Ejecutar la suite completa:

```bash
python -m pytest -v
```

Ejecutar solamente API:

```bash
python -m pytest -m api -v
```

Ejecutar pruebas POM:

```bash
python -m pytest -m pom -v
```

Ejecutar Smoke:

```bash
python -m pytest -m smoke -v
```

Ejecutar pruebas E2E:

```bash
python -m pytest -m e2e -v
```

Ejecutar BDD mediante sus wrappers de Pytest:

```bash
python -m pytest tests_behave/ -v
```

Ejecutar UI y API:

```bash
python -m pytest tests/ tests_api/ -v
```

Generar reporte HTML de la suite completa:

```bash
python -m pytest -v --html=reports/reporte_completo.html --self-contained-html
```

El archivo `pytest.ini` también configura la generación automática del reporte `reports/reporte.html`.

## 8. Configuración segura de API Key

Reqres requiere una API Key para acceder a sus endpoints protegidos.

La clave se configura mediante una variable de entorno para evitar exponer credenciales en el código fuente.

### Windows PowerShell

```powershell
$env:REQRES_API_KEY="TU_API_KEY"
```

### GitHub Actions

En el repositorio se configura un secreto llamado:

`REQRES_API_KEY`

El workflow lo utiliza mediante:

```yaml
env:
  CI: "true"
  REQRES_API_KEY: ${{ secrets.REQRES_API_KEY }}
```

**Importante:** nunca publicar la API Key en el repositorio, README, capturas o archivos de configuración versionados.

## 9. Integración continua – GitHub Actions

Se configuró un workflow en:

`.github/workflows/ci.yml`

El pipeline contempla:

1. Descarga del repositorio.
2. Configuración de Python 3.12.
3. Preparación de directorios de reportes y logs.
4. Instalación de dependencias.
5. Verificación de dependencias con `pip check`.
6. Ejecución de la suite completa UI, API y BDD mediante Pytest.
7. Almacenamiento de reportes y logs como artefactos.

El workflow se ejecuta ante eventos `push`, `pull_request` y mediante ejecución manual (`workflow_dispatch`).

## 10. Resultados de ejecución

Última ejecución completa local verificada:

**35 pruebas aprobadas – 0 fallidas.**

| Suite | Pruebas aprobadas |
|---|---:|
| Calculadora | 12 |
| Selenium / UI | 12 |
| API Testing | 7 |
| BDD / Behave mediante Pytest | 4 |
| **Total** | **35** |

La suite API comprende 6 pruebas sobre Reqres y 1 prueba E2E sobre JSONPlaceholder.

### Reportes y evidencias

Los archivos de resultados se almacenan en `reports/`:

- `reporte.html`: reporte automático generado por Pytest.
- `reporte_behave.html`: reporte HTML generado mediante Behave.
- `reporte_behave_directo.html`: reporte de una ejecución directa de Behave.
- `behave.json`: resultados de ejecución BDD.
- `screens/`: capturas de pantalla de escenarios fallidos.

También se puede generar un reporte adicional de la suite completa ejecutando:

```bash
python -m pytest -v --html=reports/reporte_completo.html --self-contained-html
```

Los registros de ejecución se almacenan en `logs/`.

## 11. Control de versiones

El proyecto utiliza Git y GitHub para el control de versiones.

Se trabaja mediante ramas de funcionalidades para organizar los cambios y mantener un historial de desarrollo.

Repositorio:

[curso-automation-testing](https://github.com/deboraciamberlini81-oss/curso-automation-testing)

## Conclusión

Este framework representa la integración de diferentes técnicas de automatización de pruebas:

- Automatización funcional de interfaces web.
- Diseño con Page Object Model.
- Pruebas basadas en datos externos.
- Parametrización de escenarios.
- Validación de servicios REST mediante Requests.
- Pruebas de ciclo de vida de recursos API.
- BDD con Behave y Gherkin.
- Organización y ejecución de suites con Pytest.
- Generación de reportes HTML y evidencias.
- Integración continua con GitHub Actions.
- Control de versiones con Git y GitHub.

El proyecto constituye una base de aprendizaje y práctica profesional en **QA Automation**, con una estructura organizada y preparada para incorporar nuevas funcionalidades, validaciones y escenarios de prueba.