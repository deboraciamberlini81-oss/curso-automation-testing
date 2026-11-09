import pytest
import requests
from datetime import datetime

BASE_URL = "https://reqres.in/api"

CASOS_CREAR_USUARIO = [
    pytest.param("Ana QA", "QA Automation Trainee", id="usuario-qa"),
    pytest.param("Carlos Tester", "Backend Developer", id="usuario-backend"),
    pytest.param("Sofia Analyst", "QA Analyst", id="usuario-analista"),
]


@pytest.mark.api
@pytest.mark.parametrize("nombre, trabajo", CASOS_CREAR_USUARIO)
def test_crear_usuario_api(nombre, trabajo):

    payload = {
        "name": nombre,
        "job": trabajo
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201, (
        f"Se esperaba 201 y se recibió {response.status_code}: "
        f"{response.text}"
    )

    datos_respuesta = response.json()

    assert datos_respuesta.get("name") == nombre
    assert datos_respuesta.get("job") == trabajo
    assert datos_respuesta.get("id")

    created_at = datos_respuesta.get("createdAt")
    assert created_at is not None

    anio_actual = str(datetime.now().year)
    assert anio_actual in created_at