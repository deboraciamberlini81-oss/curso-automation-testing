
import os
import pytest
import requests

from utils.lectura_datos import leer_json


BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")

CASOS_LOGIN = leer_json("login_api.json")


@pytest.mark.api
@pytest.mark.parametrize("caso", CASOS_LOGIN)
def test_login_api(caso):

    assert API_KEY, "Falta configurar la variable REQRES_API_KEY"

    response = requests.post(
        f"{BASE_URL}/login",
        json=caso["payload"],
        headers={"x-api-key": API_KEY},
        timeout=10
    )

    # Validar código de respuesta
    assert response.status_code == caso["status_esperado"], (
        f"Caso: {caso['nombre']} | "
        f"Status recibido: {response.status_code}"
    )

    datos_respuesta = response.json()

    # Validar presencia del token
    if caso["espera_token"]:
        assert "token" in datos_respuesta
        assert datos_respuesta["token"] != ""

    # Validar mensaje de error
    else:
        assert "error" in datos_respuesta
