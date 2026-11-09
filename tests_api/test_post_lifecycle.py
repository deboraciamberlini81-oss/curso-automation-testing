
import time

import pytest
import requests
from faker import Faker

fake = Faker()

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
TIMEOUT = 10


@pytest.mark.e2e
def test_ciclo_vida_post():

    # 1. POST: Crear un recurso
    payload = {
        "title": fake.sentence(),
        "body": fake.text()
    }

    inicio_post = time.perf_counter()

    response_post = requests.post(
        BASE_URL,
        json=payload,
        timeout=TIMEOUT
    )

    tiempo_post = time.perf_counter() - inicio_post

    assert tiempo_post < TIMEOUT, "POST superó el tiempo máximo"
    assert response_post.status_code == 201

    datos_post = response_post.json()

    # Validación de esquema y tipos
    assert isinstance(datos_post, dict)
    assert isinstance(datos_post.get("id"), int)
    assert isinstance(datos_post.get("title"), str)
    assert isinstance(datos_post.get("body"), str)

    assert datos_post["title"] == payload["title"]
    assert datos_post["body"] == payload["body"]

    post_id = datos_post["id"]

    # 2. PATCH: Actualizar el recurso
    payload_patch = {
        "title": "Título actualizado por QA"
    }

    inicio_patch = time.perf_counter()

    response_patch = requests.patch(
        f"{BASE_URL}/{post_id}",
        json=payload_patch,
        timeout=TIMEOUT
    )

    tiempo_patch = time.perf_counter() - inicio_patch

    assert tiempo_patch < TIMEOUT, "PATCH superó el tiempo máximo"
    assert response_patch.status_code == 200

    datos_patch = response_patch.json()

    # Validación de respuesta PATCH
    assert isinstance(datos_patch, dict)
    assert datos_patch.get("title") == payload_patch["title"]
    assert isinstance(datos_patch.get("title"), str)

    # JSONPlaceholder puede omitir el ID en la respuesta PATCH
    if "id" in datos_patch:
        assert datos_patch["id"] == post_id

    # 3. DELETE: Eliminar el recurso
    inicio_delete = time.perf_counter()

    response_delete = requests.delete(
        f"{BASE_URL}/{post_id}",
        timeout=TIMEOUT
    )

    tiempo_delete = time.perf_counter() - inicio_delete

    assert tiempo_delete < TIMEOUT, "DELETE superó el tiempo máximo"
    assert response_delete.status_code == 200

    # 4. Resultado del ciclo de vida
    print("\n--- QA-132: Ciclo de vida del recurso ---")
    print(f"ID creado: {post_id}")
    print(f"Título inicial: {payload['title']}")
    print(f"Título actualizado: {datos_patch['title']}")
    print(f"Tiempo POST: {tiempo_post:.3f} segundos")
    print(f"Tiempo PATCH: {tiempo_patch:.3f} segundos")
    print(f"Tiempo DELETE: {tiempo_delete:.3f} segundos")
    print("Ciclo de vida finalizado correctamente")
