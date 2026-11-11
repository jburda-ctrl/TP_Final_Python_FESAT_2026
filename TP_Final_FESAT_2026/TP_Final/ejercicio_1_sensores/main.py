from sensores import sanitizar_registro, generar_resumen_sensores, cargar_desde_csv
if __name__ == "__main__":
    lista = cargar_desde_csv("datos_sensores.csv")
    print("Registros limpios:", lista)
    alertas, promedio = generar_resumen_sensores(lista, umbral_alerta=85.0)
    print(f"Alertas (>85): {alertas}")
    print(f"Promedio: {promedio:.2f}")
