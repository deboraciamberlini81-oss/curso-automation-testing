import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.pom
@pytest.mark.smoke
def test_agregar_producto_al_carrito(driver):

    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)

    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    nombre_producto = inventario.obtener_nombre_primer_producto()

    inventario.agregar_primer_producto()

    assert inventario.obtener_contador_carrito() == "1"

    inventario.abrir_carrito()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    assert carrito.contiene_producto(nombre_producto)