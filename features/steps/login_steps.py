from behave import given, when, then


@given("que estoy en la pagina de login de SauceDemo")
def abrir_pagina_login(context):
    context.login_page.abrir()


@when('inicio sesion con usuario "{usuario}" y password "{password}"')
def iniciar_sesion(context, usuario, password):
    if usuario == "VACIO" and password == "VACIO":
        usuario = ""
        password = ""

    context.login_page.iniciar_sesion(usuario, password)

@then("debo acceder al inventario de productos")
def verificar_inventario(context):
    assert "/inventory.html" in context.driver.current_url, (
        "No se redirigio al inventario correctamente"
    )

    assert context.inventory_page.obtener_titulo() == "Products"


@then("debo visualizar el mensaje de error")
def verificar_mensaje_error(context):
    mensaje = context.login_page.obtener_mensaje_error()

    assert mensaje != "", "El mensaje de error esta vacio"

@when("intento iniciar sesion con campos vacios")
def iniciar_sesion_campos_vacios(context):
    context.login_page.iniciar_sesion("", "")