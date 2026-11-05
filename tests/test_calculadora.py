import pytest

from calculadora.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir
)


def test_sumar():
    assert sumar(10, 5) == 15


def test_restar():
    assert restar(10, 5) == 5


def test_multiplicar():
    assert multiplicar(10, 5) == 50


def test_dividir():
    assert dividir(10, 5) == 2


def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)