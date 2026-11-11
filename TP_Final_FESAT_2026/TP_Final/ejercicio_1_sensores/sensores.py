"""Ejercicio 1 - Sensores: funciones puras, sin POO."""
def sanitizar_registro(registro):
    """Limpia y estandariza un registro de sensor."""
    if not isinstance(registro, dict):
        registro = {}
    sensor_id = registro.get("sensor_id", "")
    if not sensor_id or not str(sensor_id).strip():
        sensor_id = "DESCONOCIDO"
    else:
        sensor_id = str(sensor_id).strip()
    try:
        temperatura = float(registro.get("temperatura", 0.0))
    except (ValueError, TypeError):
        temperatura = 0.0
    ubicacion = registro.get("ubicacion", "")
    if not ubicacion or not str(ubicacion).strip():
        ubicacion = "Área No Asignada"
    else:
        ubicacion = str(ubicacion).strip()
    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}

def generar_resumen_sensores(lista_limpia, umbral_alerta):
    """Devuelve (alertas, promedio). Cláusula de guarda si lista vacía."""
    if not lista_limpia:
        return ([], 0.0)
    alertas = []
    acumulador = 0.0
    for reg in lista_limpia:
        temp = reg["temperatura"]
        acumulador += temp
        if temp > umbral_alerta:  # estricto, no >=
            alertas.append(reg["sensor_id"])
    promedio = acumulador / len(lista_limpia)
    return (alertas, promedio)

def cargar_desde_csv(ruta_csv):
    """Simulacion de datos: consume CSV y sanitiza cada fila."""
    import csv
    registros = []
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            registros.append(sanitizar_registro(fila))
    return registros
