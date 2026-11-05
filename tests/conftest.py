import pytest


@pytest.fixture
def numeros_enteros():
    return 10, 5


@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2