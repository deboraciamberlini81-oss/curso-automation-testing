import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.lectura_datos import leer_json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Leer productos desde el archivo JSON
PRODUCTOS = leer_json("productos.json")


@pytest.fixture
def usuario_logueado(driver):
    """Realiza login antes de cada test de carrito."""

    login = LoginPage(driver)

    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    return driver


@pytest.mark.pom
@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    """Agrega cada producto del JSON al carrito."""

    inventario = InventoryPage(usuario_logueado)
    carrito = CartPage(usuario_logueado)

    inventario.agregar_producto_por_xpath(producto["xpath"])

    assert inventario.obtener_contador_carrito() == "1"

    inventario.abrir_carrito()

    WebDriverWait(usuario_logueado, 10).until(
        EC.url_contains("/cart.html")
    )

    assert carrito.contiene_producto(producto["nombre"])


@pytest.mark.pom
@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    """Verifica la funcionalidad básica del carrito."""

    inventario = InventoryPage(usuario_logueado)

    inventario.agregar_primer_producto()

    assert inventario.obtener_contador_carrito() == "1"

    inventario.abrir_carrito()

    WebDriverWait(usuario_logueado, 10).until(
        EC.url_contains("/cart.html")
    )

    assert "/cart.html" in usuario_logueado.current_url