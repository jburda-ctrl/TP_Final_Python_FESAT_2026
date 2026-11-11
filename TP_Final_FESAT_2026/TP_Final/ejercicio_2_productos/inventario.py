from producto import Producto
class Inventario:
    def __init__(self, nombre="Inventario General"):
        self.nombre = nombre
        self.__productos = []
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto): raise TypeError("Solo se admiten Producto")
        self.__productos.append(producto)
    def obtener_productos(self): return list(self.__productos)
    def buscar_por_codigo(self, codigo):
        for p in self.__productos:
            if p.codigo == codigo: return p
        return None
    def valor_total_inventario(self): return sum(p.valor_total() for p in self.__productos)
    def productos_bajo_stock(self, umbral=5): return [p for p in self.__productos if p.stock < umbral]
    def __len__(self): return len(self.__productos)
