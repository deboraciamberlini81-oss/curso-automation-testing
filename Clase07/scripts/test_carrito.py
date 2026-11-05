
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_producto_al_carrito():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Iniciar sesión
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # 3. Esperar el inventario
        wait.until(EC.url_contains("/inventory.html"))

        # 4. Obtener el primer producto
        productos = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.inventory_item")
            )
        )

        primer_producto = productos[0]

        nombre = primer_producto.find_element(
            By.CSS_SELECTOR,
            ".inventory_item_name"
        ).text

        # 5. Agregar el primer producto al carrito
        primer_producto.find_element(
            By.CSS_SELECTOR,
            "button.btn_inventory"
        ).click()

        # 6. Verificar que el contador muestre 1
        contador = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".shopping_cart_badge")
            )
        )

        assert contador.text == "1"

        # 7. Entrar al carrito
        driver.find_element(
            By.CSS_SELECTOR,
            ".shopping_cart_link"
        ).click()

        wait.until(EC.url_contains("/cart.html"))

        # 8. Comprobar que el producto esté listado
        producto_carrito = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
            )
        )

        assert producto_carrito.text == nombre

        print(f"Producto agregado: {nombre}")
        print("Test OK")

    finally:
        driver.quit()
