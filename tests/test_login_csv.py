import pytest

from pages.login_page import LoginPage
from utils.lectura_datos import leer_csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Leer los casos desde el archivo CSV
usuarios = leer_csv("login.csv")


# Separar el usuario válido que utilizaremos para Smoke
datos_login_smoke = next(
    datos for datos in usuarios
    if datos["usuario"] == "standard_user"
    and datos["password"] == "secret_sauce"
    and datos["resultado_esperado"] == "exitoso"
)


# Dejar los otros cinco casos para la prueba parametrizada
usuarios_parametrizados = [
    datos for datos in usuarios
    if datos != datos_login_smoke
]


@pytest.mark.pom
@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):

    login = LoginPage(driver)

    login.abrir()

    login.iniciar_sesion(
        datos_login_smoke["usuario"],
        datos_login_smoke["password"]
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"


@pytest.mark.pom
@pytest.mark.parametrize("datos_usuario", usuarios_parametrizados)
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

    else:
        pytest.fail(
            f"Resultado esperado desconocido: {resultado_esperado}"
        )