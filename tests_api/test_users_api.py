
import os
import requests
import pytest


BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")


@pytest.mark.api
def test_obtener_usuarios():

    assert API_KEY, "Falta configurar la variable REQRES_API_KEY"

    response = requests.get(
        f"{BASE_URL}/users",
        params={"page": 1},
        headers={"x-api-key": API_KEY},
        timeout=10
    )

    # Validar código HTTP
    assert response.status_code == 200

    datos = response.json()

    # Validar estructura de respuesta
    assert "data" in datos
    assert len(datos["data"]) > 0

    # Validar datos del primer usuario
    usuario = datos["data"][0]

    assert "id" in usuario
    assert "email" in usuario
    assert "first_name" in usuario
