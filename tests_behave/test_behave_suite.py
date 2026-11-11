
import subprocess
import json
import sys
from pathlib import Path

import pytest


# Directorio principal del proyecto
ROOT_DIR = Path(__file__).resolve().parents[1]

# Directorio donde se guardarán los reportes
REPORTS_DIR = ROOT_DIR / "reports"

def corregir_resumen_html(ruta_json, ruta_html):
    """Actualiza los contadores HTML según los estados reales del JSON."""

    import re

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    estados = ["passed", "failed", "skipped", "untested"]

    features = {estado: 0 for estado in estados}
    escenarios = {estado: 0 for estado in estados}
    pasos = {estado: 0 for estado in estados}

    for feature in datos:
        escenarios_feature = []

        for elemento in feature.get("elements", []):
            if elemento.get("type") not in ("scenario", "scenario_outline"):
                continue

            estados_pasos = []

            for paso in elemento.get("steps", []):
                estado = paso.get("result", {}).get("status", "untested")

                if estado not in pasos:
                    estado = "untested"

                pasos[estado] += 1
                estados_pasos.append(estado)

            if "failed" in estados_pasos:
                estado_escenario = "failed"
            elif "untested" in estados_pasos:
                estado_escenario = "untested"
            elif "skipped" in estados_pasos:
                estado_escenario = "skipped"
            else:
                estado_escenario = "passed"

            escenarios[estado_escenario] += 1
            escenarios_feature.append(estado_escenario)

        if "failed" in escenarios_feature:
            estado_feature = "failed"
        elif "untested" in escenarios_feature:
            estado_feature = "untested"
        elif escenarios_feature and all(
            estado == "skipped" for estado in escenarios_feature
        ):
            estado_feature = "skipped"
        else:
            estado_feature = "passed"

        features[estado_feature] += 1

    def construir_resumen(nombre, resultados):
        detalle = ", ".join(
            f"{estado}: {cantidad}"
            for estado, cantidad in resultados.items()
            if cantidad > 0
        )
        return f"{nombre}: {detalle}"

    with open(ruta_html, "r", encoding="utf-8") as archivo:
        html = archivo.read()

    resumenes = {
        "feature_totals": construir_resumen("Features", features),
        "scenario_totals": construir_resumen("Scenarios", escenarios),
        "step_totals": construir_resumen("Steps", pasos)
    }

    for identificador, resumen in resumenes.items():
        html = re.sub(
            rf'(<p id="{identificador}">).*?(</p>)',
            lambda coincidencia: (
                coincidencia.group(1) + resumen + coincidencia.group(2)
            ),
            html
        )

    with open(ruta_html, "w", encoding="utf-8") as archivo:
        archivo.write(html)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def ejecutar_behave(*argumentos):
    """Ejecuta Behave desde Pytest y devuelve el resultado."""

    comando = [
        sys.executable,
        "-m",
        "behave",
        *argumentos
    ]

    return subprocess.run(
    comando,
    cwd=ROOT_DIR,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace"
)
@pytest.mark.bdd
@pytest.mark.smoke
def test_behave_smoke():
    """Ejecuta los escenarios marcados como smoke."""

    resultado = ejecutar_behave(
        "--tags", "@smoke",
        "--format", "pretty"
    )

    assert resultado.returncode == 0, (
        "Falló la ejecución de Behave:\n"
        f"{resultado.stdout}\n"
        f"{resultado.stderr}"
    )

@pytest.mark.bdd
@pytest.mark.regression
def test_behave_regression():
    """Ejecuta los escenarios marcados como regression."""

    resultado = ejecutar_behave(
        "--tags", "@regression",
        "--format", "pretty"
    )

    assert resultado.returncode == 0, (
        "Falló la ejecución de Behave:\n"
        f"{resultado.stdout}\n"
        f"{resultado.stderr}"
    )

@pytest.mark.bdd
def test_behave_reporte_json():
    """Ejecuta toda la suite y genera un reporte JSON."""

    ruta_json = REPORTS_DIR / "behave.json"

    resultado = ejecutar_behave(
        "--format", "json",
        "--outfile", str(ruta_json),
        "--format", "pretty"
    )

    assert resultado.returncode == 0, (
        "Falló la ejecución de Behave:\n"
        f"{resultado.stdout}\n"
        f"{resultado.stderr}"
    )

    assert ruta_json.exists(), "No se generó el reporte JSON"
    assert ruta_json.stat().st_size > 0, "El reporte JSON está vacío"

@pytest.mark.bdd
def test_behave_reporte_html():
    """Genera los reportes JSON y HTML y corrige sus contadores."""

    ruta_json = REPORTS_DIR / "behave.json"
    ruta_html = REPORTS_DIR / "reporte_behave.html"

    resultado = ejecutar_behave(
        "--format", "json",
        "--outfile", str(ruta_json),
        "--format", "html",
        "--outfile", str(ruta_html)
    )

    assert resultado.returncode == 0, (
        "Falló la ejecución de Behave:\n"
        f"{resultado.stdout}\n"
        f"{resultado.stderr}"
    )

    assert ruta_json.exists(), "No se generó el reporte JSON"
    assert ruta_html.exists(), "No se generó el reporte HTML"

    corregir_resumen_html(ruta_json, ruta_html)

    assert ruta_html.stat().st_size > 0, "El reporte HTML está vacío"