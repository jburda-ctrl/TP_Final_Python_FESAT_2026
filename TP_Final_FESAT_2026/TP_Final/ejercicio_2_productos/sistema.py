from inventario import Inventario
class AlertaStock:
    def __init__(self, mensaje, nivel="MEDIA"):
        self.__mensaje = mensaje
        self.__nivel = nivel
    @property
    def nivel(self): return self.__nivel
    @nivel.setter
    def nivel(self, v): self.__nivel = str(v).upper()
    def mostrar_alerta(self): print(f"[{self.__nivel}] {self.__mensaje}")
    def __str__(self): return f"[{self.__nivel}] {self.__mensaje}"

class SistemaProductos(Inventario):
    """Hereda de Inventario y agrega monitoreo de alertas."""
    def __init__(self, nombre="Sistema Productos", umbral_alerta=5):
        super().__init__(nombre)
        self.umbral_alerta = umbral_alerta
        self.alertas_activas = []
    def verificar_alertas(self):
        self.alertas_activas = []
        for p in self.obtener_productos():
            if p.stock < self.umbral_alerta:
                a = AlertaStock(f"Stock bajo: {p.nombre} ({p.stock} u.)", "ALTA")
                self.alertas_activas.append(a)
        return self.alertas_activas
    def generar_informe(self):
        print(f"=== {self.nombre} ===")
        print(f"Productos: {len(self)} | Valor total: ${self.valor_total_inventario():.2f}")
        for p in self.obtener_productos(): print(" -", p)
        for a in self.verificar_alertas(): a.mostrar_alerta()
