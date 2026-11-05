
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_saucedemo():

    driver = webdriver.Chrome()

    try:
        # 1. Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Ingresar credenciales
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

        # 3. Hacer clic en Login
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # 4. Esperar la redirección al inventario
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        # 5. Validar la URL
        assert "/inventory.html" in driver.current_url

        # 6. Validar el título de la página
        titulo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.header_secondary_container .title")
            )
        )

        assert titulo.text == "Products"

        print("Test OK")

    finally:
        driver.quit()
