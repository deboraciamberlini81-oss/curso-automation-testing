
import pytest

from pages.login_page import LoginPage
from utils.lectura_datos import leer_csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usuarios = leer_csv("login.csv")


@pytest.mark.pom
@pytest.mark.smoke
@pytest.mark.parametrize("datos_usuario", usuarios)
def test_login_parametrizado(driver, datos_usuario):

    login = LoginPage(driver)

    login.abrir()

    login.iniciar_sesion(
        datos_usuario["usuario"],
        datos_usuario["password"]
    )

    resultado_esperado = datos_usuario["resultado_esperado"]

    if resultado_esperado == "exitoso":

        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        assert "/inventory.html" in driver.current_url
        assert driver.title == "Swag Labs"

    elif resultado_esperado == "bloqueado":

        mensaje = login.obtener_mensaje_error()

        assert "locked out" in mensaje.lower()

    elif resultado_esperado == "error":

        mensaje = login.obtener_mensaje_error()

        assert mensaje != ""
