import pytest

from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.pom
@pytest.mark.smoke
def test_login_exitoso(driver):

    login = LoginPage(driver)

    login.abrir()
    login.iniciar_sesion("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url

    assert driver.title == "Swag Labs"