# Clase 07 – Automatización de flujos con Selenium

## Objetivo

Automatizar los principales flujos de navegación de la aplicación web SauceDemo utilizando Selenium WebDriver y Pytest.

## Herramientas utilizadas

- Python
- Selenium 4
- Pytest
- Google Chrome
- Visual Studio Code

## Estructura del proyecto

```text
Clase07/
│
├── README.md
│
└── scripts/
    ├── test_login.py
    ├── test_inventario.py
    └── test_carrito.py
```

## Pruebas automatizadas

### 1. Login (`test_login.py`)
- Abrir SauceDemo.
- Ingresar credenciales válidas.
- Validar la redirección a `/inventory.html`.
- Verificar que el título sea `Products`.

### 2. Inventario (`test_inventario.py`)
- Validar el título `Products`.
- Comprobar que existan productos.
- Obtener el nombre y precio del primer producto.

### 3. Carrito (`test_carrito.py`)
- Agregar el primer producto al carrito.
- Validar que el contador indique `1`.
- Ingresar al carrito.
- Comprobar que el producto agregado esté listado.

## Ejecución de las pruebas

Ejecutar todas las pruebas desde la carpeta raíz del proyecto:

```powershell
python -m pytest -v .\Clase07\scripts -s
```

## Resultado obtenido

**3 pruebas aprobadas (3 passed).**

Los tres flujos automatizados funcionaron correctamente durante la ejecución conjunta.

## Conclusión

Se implementaron y validaron tres flujos fundamentales de automatización web utilizando Selenium WebDriver y Pytest. Estos scripts constituyen una base para continuar desarrollando el proyecto de automatización en la Clase 08.