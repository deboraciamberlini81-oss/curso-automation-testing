import pytest

from calculadora.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir
)


# PRUEBAS DE SUMA
@pytest.mark.smoke
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 15),
        (20, 10, 30),
        (3, 7, 10)
    ]
)
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.smoke
def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert sumar(a, b) == pytest.approx(0.3)


# PRUEBAS DE RESTA
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 5),
        (20, 10, 10),
        (7, 3, 4)
    ]
)
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado


def test_restar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) == 5


# PRUEBAS DE MULTIPLICACIÓN
def test_multiplicar(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 50


def test_multiplicar_error():
    with pytest.raises(TypeError):
        multiplicar("texto", 2.5)


# PRUEBAS DE DIVISIÓN
def test_dividir(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 2


@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)