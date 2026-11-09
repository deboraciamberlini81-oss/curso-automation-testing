from behave import when, then


@when('agrego el producto "{nombre}" al carrito')
def agregar_producto(context, nombre):
    xpath = (
        f"//div[contains(@class,'inventory_item')]"
        f"[.//div[contains(@class,'inventory_item_name') "
        f"and normalize-space(.)='{nombre}']]"
        f"//button[contains(@class,'btn_inventory')]"
    )

    context.inventory_page.agregar_producto_por_xpath(xpath)

@then('el contador del carrito debe mostrar "{cantidad}"')
def verificar_contador(context, cantidad):
    contador = context.inventory_page.obtener_contador_carrito()

    assert contador == cantidad, (
        f"Se esperaba {cantidad}, pero el contador muestra {contador}"
    )


@then('el carrito debe contener el producto "{nombre}"')
def verificar_producto_carrito(context, nombre):
    context.inventory_page.abrir_carrito()

    assert context.cart_page.contiene_producto(nombre), (
        f"El producto {nombre} no se encuentra en el carrito"
    )