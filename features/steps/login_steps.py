
import logging

from behave import given, when, then


logger = logging.getLogger(__name__)


@given("que estoy en la pagina de login de SauceDemo")
def abrir_pagina_login(context):
    logger.info("Abriendo pagina de login de SauceDemo")
    context.login_page.abrir()


@when('inicio sesion con usuario "{usuario}" y password "{password}"')
def iniciar_sesion(context, usuario, password):
    logger.info("Iniciando sesion con usuario: %s", usuario)

    if usuario == "VACIO" and password == "VACIO":
        usuario = ""
        password = ""

    context.login_page.iniciar_sesion(usuario, password)


@then("debo acceder al inventario de productos")
def verificar_inventario(context):
    logger.info("Verificando acceso al inventario")

    assert "/inventory.html" in context.driver.current_url, (
        "No se redirigio al inventario correctamente"
    )

    assert context.inventory_page.obtener_titulo() == "Products"


@then("debo visualizar el mensaje de error")
def verificar_mensaje_error(context):
    logger.info("Verificando mensaje de error de login")

    mensaje = context.login_page.obtener_mensaje_error()

    assert mensaje != "", "El mensaje de error esta vacio"
