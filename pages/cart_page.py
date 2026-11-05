from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    PRODUCTOS_CARRITO = (By.CSS_SELECTOR, ".cart_item")
    NOMBRE_PRODUCTO = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTOS_CARRITO)
        )

    def obtener_nombre_primer_producto(self):
        producto = self.obtener_productos()[0]
        return producto.find_element(
            *self.NOMBRE_PRODUCTO
        ).text

    def contiene_producto(self, nombre):
        return any(
            producto.find_element(*self.NOMBRE_PRODUCTO).text == nombre
            for producto in self.obtener_productos()
        )