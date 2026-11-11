from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    TITULO = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTOS = (By.CSS_SELECTOR, "div.inventory_item")
    NOMBRE_PRODUCTO = (By.CSS_SELECTOR, ".inventory_item_name")
    PRECIO_PRODUCTO = (By.CSS_SELECTOR, ".inventory_item_price")
    BOTON_AGREGAR = (By.CSS_SELECTOR, "button.btn_inventory")
    CARRITO = (By.CSS_SELECTOR, ".shopping_cart_link")
    CONTADOR_CARRITO = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.TITULO)
        )
        return elemento.text

    def obtener_productos(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTOS)
        )

    def obtener_nombre_primer_producto(self):
        producto = self.obtener_productos()[0]
        return producto.find_element(
            *self.NOMBRE_PRODUCTO
        ).text

    def obtener_precio_primer_producto(self):
        producto = self.obtener_productos()[0]
        return producto.find_element(
            *self.PRECIO_PRODUCTO
        ).text

    def agregar_primer_producto(self):
        producto = self.obtener_productos()[0]
        producto.find_element(*self.BOTON_AGREGAR).click()
        
    def agregar_producto_por_xpath(self, xpath):
        boton = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, xpath))
        )
        boton.click()

    def obtener_contador_carrito(self):
        contador = self.wait.until(
            EC.visibility_of_element_located(self.CONTADOR_CARRITO)
        )
        return contador.text

    def abrir_carrito(self):
        self.driver.find_element(*self.CARRITO).click()