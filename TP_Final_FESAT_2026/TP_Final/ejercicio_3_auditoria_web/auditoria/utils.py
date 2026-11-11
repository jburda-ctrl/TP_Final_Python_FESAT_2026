"""Logica auditada - Ejercicio 3. Reutilizable y testeable sin Django."""
import csv, json
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent

def calcular_recargo_exceso(litros_consumidos, precio_litro=1.5):
    if litros_consumidos < 0:
        raise ValueError("El volumen de consumo de agua no puede ser negativo.")
    if litros_consumidos <= 100:
        return litros_consumidos * precio_litro
    exceso = litros_consumidos - 100
    return (100 * precio_litro) + (exceso * precio_litro * 1.5)

def obtener_metricas_totales(registros):
    if not registros:
        return {"costo_total_global": 0, "planta_mayor_consumo": "Ninguna"}
    total = 0; max_c = -1; planta = ""
    for reg in registros:
        c = reg["consumo"]
        total += calcular_recargo_exceso(c)
        if c > max_c:
            max_c = c; planta = reg["planta"]
    return {"costo_total_global": total, "planta_mayor_consumo": planta}

def cargar_datos_csv(nombre="datos_consumo.csv"):
    out = []
    with open(BASE / nombre, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            out.append({"planta": fila["planta"], "consumo": int(fila["consumo"])})
    return out

def cargar_datos_json(nombre="datos_consumo.json"):
    with open(BASE / nombre, encoding="utf-8") as f:
        return json.load(f)

def cargar_datos(fuente="csv"):
    """Simulacion: CSV por defecto, JSON o dict inventado como alternativa."""
    if fuente == "json":
        return cargar_datos_json()
    if fuente == "dict":
        return [{"planta": "Planta Textil Norte", "consumo": 150}, {"planta": "Destilería Sur", "consumo": 80}, {"planta": "Sede Central", "consumo": 200}]
    return cargar_datos_csv()
