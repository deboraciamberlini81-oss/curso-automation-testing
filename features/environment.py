import os
from datetime import datetime
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("reports", exist_ok=True)

        nombre = (
            f"{scenario.name.replace(' ', '_')}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )

        ruta = os.path.join("reports", nombre)
        context.driver.save_screenshot(ruta)

        print(f"Screenshot guardada: {ruta}")

    context.driver.quit()