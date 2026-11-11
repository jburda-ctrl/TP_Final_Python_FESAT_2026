from producto import Producto
class ProductoPerecedero(Producto):
    """Herencia + polimorfismo: redefine valor_total con descuento por vencimiento."""
    def __init__(self, codigo, nombre, precio, stock, dias_para_vencer):
        super().__init__(codigo, nombre, precio, stock)
        self.__dias_para_vencer = int(dias_para_vencer)
    @property
    def dias_para_vencer(self): return self.__dias_para_vencer
    def esta_vencido(self): return self.__dias_para_vencer <= 0
    def valor_total(self):
        # Polimorfismo: si vence en <=3 dias, 50% de descuento
        base = super().valor_total()
        if self.esta_vencido(): return 0.0
        if self.__dias_para_vencer <= 3: return base * 0.5
        return base
    def __str__(self): return super().__str__() + f" [Vence en {self.__dias_para_vencer} dias]"
