"""Clase base Producto con encapsulamiento."""
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = str(codigo).strip() if codigo else "SIN-CODIGO"
        self.__nombre = str(nombre).strip()
        self.__precio = float(precio) if float(precio) >= 0 else 0.0
        self.__stock = int(stock) if int(stock) >= 0 else 0
    @property
    def codigo(self): return self.__codigo
    @property
    def nombre(self): return self.__nombre
    @property
    def precio(self): return self.__precio
    @precio.setter
    def precio(self, valor):
        if valor < 0: raise ValueError("El precio no puede ser negativo")
        self.__precio = float(valor)
    @property
    def stock(self): return self.__stock
    def actualizar_stock(self, cantidad):
        nuevo = self.__stock + int(cantidad)
        if nuevo < 0: raise ValueError("Stock insuficiente")
        self.__stock = nuevo
    def valor_total(self): return self.__precio * self.__stock
    def __str__(self): return f"{self.__codigo} - {self.__nombre} (${self.__precio:.2f} x {self.__stock})"
    def __repr__(self): return f"Producto({self.__codigo!r}, {self.__nombre!r}, {self.__precio}, {self.__stock})"
    def __eq__(self, otro): return isinstance(otro, Producto) and self.__codigo == otro.codigo
