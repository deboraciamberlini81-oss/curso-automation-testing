
import os
import pytest
from datetime import datetime
from selenium import webdriver


@pytest.fixture
def numeros_enteros():
    return 10, 5


@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")

        if navegador is not None:
            carpeta = "reports"
            os.makedirs(carpeta, exist_ok=True)

            nombre = (
                f"{item.name}_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

            ruta = os.path.join(carpeta, nombre)

            navegador.save_screenshot(ruta)

            print(f"\nCaptura de pantalla guardada: {ruta}")