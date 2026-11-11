
import os
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

    # Configuración de Chrome
    opciones = Options()

    if os.getenv("CI") == "true":
        opciones.add_argument("--headless=new")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")
        opciones.add_argument("--window-size=1920,1080")

    opciones.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    # Inicialización del navegador
    context.driver = webdriver.Chrome(options=opciones)
    context.driver.maximize_window()

    # Inicialización de Page Objects
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)

    logger.info("WebDriver y Page Objects inicializados correctamente")


def before_scenario(context, scenario):
    """Registra el inicio de cada escenario."""

    logger.info(
        "Iniciando escenario: %s",
        scenario.name
    )

    context.driver.delete_all_cookies()


def after_step(context, step):
    """Captura una pantalla automáticamente cuando falla un step."""

    if step.status in ("failed", "error"):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        scenario = context.scenario.name.split("--")[-1].strip()
        scenario = scenario.replace(" ", "_")

        step_name = step.name[:25].replace(" ", "_")

        nombre_archivo = (
            f"{scenario}_{step_name}_{timestamp}.png"
        )

        ruta = os.path.join(
            "reports",
            "screens",
            nombre_archivo
        )

        context.driver.save_screenshot(ruta)

        logger.error("Step fallido: %s", step.name)
        logger.info("Screenshot guardada en: %s", ruta)


def after_all(context):
    """Cierra el navegador y libera los recursos."""

    if getattr(context, "driver", None):
        context.driver.quit()
        logger.info("WebDriver cerrado correctamente")

    logger.info("Finalizada la ejecución del framework BDD")
