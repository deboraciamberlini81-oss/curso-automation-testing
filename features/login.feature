@ui
Feature: Autenticacion de usuarios en SauceDemo

  Como usuario de SauceDemo
  Quiero iniciar sesion
  Para acceder al inventario de productos

  Background:
    Given que estoy en la pagina de login de SauceDemo

  @smoke
  Scenario: Login exitoso con credenciales validas
    When inicio sesion con usuario "standard_user" y password "secret_sauce"
    Then debo acceder al inventario de productos

  @regression
  Scenario Outline: Login fallido con diferentes credenciales
    When inicio sesion con usuario "<usuario>" y password "<password>"
    Then debo visualizar el mensaje de error

    Examples:
      | usuario          | password     |
      | usuario_invalido | secret_sauce |
      | locked_out_user  | secret_sauce |
      | VACIO            | VACIO        |