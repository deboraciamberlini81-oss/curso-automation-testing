
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    # Localizadores
    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def iniciar_sesion(self, usuario, password):

        campo_usuario = self.wait.until(
            EC.element_to_be_clickable(self.INPUT_USUARIO)
        )
        campo_usuario.clear()

        if usuario:
            campo_usuario.send_keys(usuario)

        campo_password = self.wait.until(
            EC.element_to_be_clickable(self.INPUT_PASSWORD)
        )
        campo_password.clear()

        if password:
            campo_password.send_keys(password)

        boton = self.wait.until(
            EC.element_to_be_clickable(self.BOTON_LOGIN)
        )
        boton.click()

    def obtener_mensaje_error(self):

        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE_ERROR)
        )

        return mensaje.text
