
import logging

from behave import when, then


logger = logging.getLogger(__name__)


@when('agrego el producto "{nombre}" al carrito')
def agregar_producto(context, nombre):
    logger.info("Agregando producto al carrito: %s", nombre)

    xpath = (
        f"//div[contains(@class,'inventory_item')]"
        f"[.//div[contains(@class,'inventory_item_name') "
        f"and normalize-space(.)='{nombre}']]"
        f"//button[contains(@class,'btn_inventory')]"
    )

    context.inventory_page.agregar_producto_por_xpath(xpath)


@then('el contador del carrito debe mostrar "{cantidad}"')
def verificar_contador(context, cantidad):
    logger.info("Verificando contador del carrito: %s", cantidad)

    contador = context.inventory_page.obtener_contador_carrito()

    assert contador == cantidad, (
        f"Se esperaba {cantidad}, pero el contador muestra {contador}"
    )


@then('el carrito debe contener el producto "{nombre}"')
def verificar_producto_carrito(context, nombre):
    logger.info("Verificando que el carrito contenga: %s", nombre)

    context.inventory_page.abrir_carrito()

    assert context.cart_page.contiene_producto(nombre), (
        f"El producto {nombre} no se encuentra en el carrito"
    )
