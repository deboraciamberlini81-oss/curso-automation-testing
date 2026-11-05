import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.pom
@pytest.mark.smoke
def test_catalogo_muestra_productos(driver):

    login = LoginPage(driver)
    inventario = InventoryPage(driver)

    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")

    assert inventario.obtener_titulo() == "Products"

    productos = inventario.obtener_productos()

    assert len(productos) >= 1

    nombre = inventario.obtener_nombre_primer_producto()
    precio = inventario.obtener_precio_primer_producto()

    assert nombre != ""
    assert precio != ""

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")