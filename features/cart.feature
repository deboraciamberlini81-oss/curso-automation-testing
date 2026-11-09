@ui
Feature: Gestion del carrito de compras

  Como usuario de SauceDemo
  Quiero agregar productos al carrito
  Para poder realizar una compra

  Background:
    Given que estoy en la pagina de login de SauceDemo
    When inicio sesion con usuario "standard_user" y password "secret_sauce"
    Then debo acceder al inventario de productos

  @regression
  Scenario: Agregar Sauce Labs Backpack al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito debe mostrar "1"
    And el carrito debe contener el producto "Sauce Labs Backpack"