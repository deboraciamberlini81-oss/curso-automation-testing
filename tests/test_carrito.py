import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.lectura_datos import leer_json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


productos = leer_json("productos.json")


@pytest.mark.pom
@pytest.mark.smoke
@pytest.mark.parametrize("datos_producto", productos)
def test_agregar_producto_al_carrito(driver, datos_producto):

    login = LoginPage(driver)
    inventario = InventoryPage(driver)
    carrito = CartPage(driver)

    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventario.agregar_producto_por_xpath(datos_producto["xpath"])

    assert inventario.obtener_contador_carrito() == "1"

    inventario.abrir_carrito()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    assert carrito.contiene_producto(datos_producto["nombre"])