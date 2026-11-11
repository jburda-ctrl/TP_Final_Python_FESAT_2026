import pytest
from .utils import calcular_recargo_exceso, obtener_metricas_totales, cargar_datos
def test_sin_exceso():
    assert calcular_recargo_exceso(50, 1.5) == 75.0
def test_con_exceso():
    assert calcular_recargo_exceso(120, 1.5) == 195.0
def test_negativo():
    with pytest.raises(ValueError):
        calcular_recargo_exceso(-10, 1.5)
def test_metricas_vacias():
    assert obtener_metricas_totales([]) == {"costo_total_global": 0, "planta_mayor_consumo": "Ninguna"}
def test_metricas_totales_ejemplo():
    datos = [{"planta": "Planta Textil Norte", "consumo": 150}, {"planta": "Destilería Sur", "consumo": 80}, {"planta": "Sede Central", "consumo": 200}]
    m = obtener_metricas_totales(datos)
    assert m["costo_total_global"] == 757.5
    assert m["planta_mayor_consumo"] == "Sede Central"
def test_cargar_csv():
    assert len(cargar_datos("csv")) == 3
def test_cargar_json_y_dict():
    assert len(cargar_datos("json")) == 3
    assert len(cargar_datos("dict")) == 3
@pytest.mark.django_db
def test_dashboard_status_200(client):
    resp = client.get("/agua/dashboard/")
    assert resp.status_code == 200
    assert b"Sede Central" in resp.content
    assert b"757.50" in resp.content
