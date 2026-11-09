import pytest
import requests


BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_obtener_usuarios():

    response = requests.get(
        f"{BASE_URL}/users",
        params={"page": 1},
        timeout=10
    )

    # Validar código HTTP
    assert response.status_code == 200

    datos_respuesta = response.json()

    # Validar que exista la lista de usuarios
    assert "data" in datos_respuesta
    usuarios = datos_respuesta["data"]
    assert len(usuarios) > 0

    # Validar estructura de cada usuario
    for usuario in usuarios:

        assert "id" in usuario
        assert "email" in usuario
        assert "first_name" in usuario
        assert "last_name" in usuario

        # Validación extra: avatar JPG
        assert usuario["avatar"].lower().endswith(".jpg")