import pytest
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