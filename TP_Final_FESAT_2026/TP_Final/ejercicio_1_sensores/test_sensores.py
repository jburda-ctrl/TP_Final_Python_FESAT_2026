from sensores import sanitizar_registro, generar_resumen_sensores
def test_sanitizar_id_vacio():
    assert sanitizar_registro({"sensor_id":"","temperatura":"20","ubicacion":" "})["sensor_id"]=="DESCONOCIDO"
def test_sanitizar_temperatura_invalida():
    assert sanitizar_registro({"sensor_id":"X","temperatura":"abc","ubicacion":"A"})["temperatura"]==0.0
def test_sanitizar_ubicacion_vacia():
    assert sanitizar_registro({"sensor_id":"X","temperatura":10,"ubicacion":"   "})["ubicacion"]=="Área No Asignada"
def test_resumen_vacio():
    assert generar_resumen_sensores([], 80)==([], 0.0)
def test_resumen_alertas_y_promedio():
    datos=[{"sensor_id":"A","temperatura":90.0,"ubicacion":"X"},{"sensor_id":"B","temperatura":70.0,"ubicacion":"Y"}]
    alertas, prom = generar_resumen_sensores(datos, 85.0)
    assert alertas==["A"] and prom==80.0
def test_umbral_estricto():
    datos=[{"sensor_id":"A","temperatura":85.0,"ubicacion":"X"}]
    assert generar_resumen_sensores(datos, 85.0)[0]==[]
