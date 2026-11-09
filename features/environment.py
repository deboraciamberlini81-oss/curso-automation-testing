
import os
import logging
from datetime import datetime

from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


logger = logging.getLogger(__name__)


def before_all(context):
    """Configura el WebDriver una sola vez para toda la ejecución."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    os.makedirs("reports/screens", exist_ok=True)

    logger.info("Iniciando framework BDD - QA Automation")

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)

    logger.info("WebDriver y Page Objects inicializados correctamente")

def before_scenario(context, scenario):
    """Limpia la sesion antes de cada escenario."""

    context.driver.delete_all_cookies()

    logger.info(
        "Iniciando escenario: %s",
        scenario.name
    )



def after_step(context, step):
    """Captura una pantalla automáticamente cuando falla un step."""

    if step.status == "failed":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        feature = context.feature.name.replace(" ", "_")
        scenario = context.scenario.name.replace(" ", "_")
        step_name = step.name.replace(" ", "_")

        nombre_archivo = (
            f"{feature}_{scenario}_{step_name}_{timestamp}.png"
        )

        ruta = os.path.join("reports", "screens", nombre_archivo)

        context.driver.save_screenshot(ruta)

        logger.error("Step fallido: %s", step.name)
        logger.info("Screenshot guardada en: %s", ruta)


def after_all(context):
    """Cierra el navegador y libera los recursos."""

    if getattr(context, "driver", None):
        context.driver.quit()
        logger.info("WebDriver cerrado correctamente")

    logger.info("Finalizada la ejecución del framework BDD")
