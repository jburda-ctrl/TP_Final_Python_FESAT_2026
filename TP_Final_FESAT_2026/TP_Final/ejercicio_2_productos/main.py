from producto import Producto
from producto_perecedero import ProductoPerecedero
from sistema import SistemaProductos
if __name__ == "__main__":
    s = SistemaProductos("Deposito Central", umbral_alerta=5)
    s.agregar_producto(Producto("P-001","Tela Algodon", 1500.0, 20))
    s.agregar_producto(Producto("P-002","Hilo Industrial", 450.0, 3))
    s.agregar_producto(ProductoPerecedero("P-003","Tinta Textil", 800.0, 10, dias_para_vencer=2))
    s.generar_informe()
