from selenium.webdriver.common.by import By


class LoginPage:

    URL = "https://www.saucedemo.com/"

    # Localizadores
    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def iniciar_sesion(self, usuario, password):
        self.driver.find_element(*self.INPUT_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BOTON_LOGIN).click()