
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
        self.driver.find_element(*self.INPUT_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BOTON_LOGIN).click()

    def obtener_mensaje_error(self):
        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE_ERROR)
        )
        return mensaje.text
