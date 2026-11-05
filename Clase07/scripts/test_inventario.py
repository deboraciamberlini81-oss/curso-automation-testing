
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explorar_inventario():

    driver = webdriver.Chrome()

    try:
        # 1. Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Iniciar sesión
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # 3. Esperar que cargue el inventario
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        # 4. Validar el título Products
        titulo = driver.find_element(
            By.CSS_SELECTOR,
            "div.header_secondary_container .title"
        )

        assert titulo.text == "Products"

        # 5. Comprobar que exista al menos un producto
        productos = driver.find_elements(
            By.CSS_SELECTOR,
            "div.inventory_item"
        )

        assert len(productos) >= 1

        # 6. Obtener nombre y precio del primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(
            By.CSS_SELECTOR,
            ".inventory_item_name"
        ).text

        precio = primer_producto.find_element(
            By.CSS_SELECTOR,
            ".inventory_item_price"
        ).text

        print(f"Primer producto: {nombre}")
        print(f"Precio: {precio}")

    finally:
        driver.quit()
