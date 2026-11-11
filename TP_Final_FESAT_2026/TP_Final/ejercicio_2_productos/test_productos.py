import pytest
from producto import Producto
from producto_perecedero import ProductoPerecedero
from sistema import SistemaProductos
def test_precio_negativo():
    with pytest.raises(ValueError): p=Producto("X","A",10,1); p.precio=-5
def test_stock_insuficiente():
    p=Producto("X","A",10,1)
    with pytest.raises(ValueError): p.actualizar_stock(-5)
def test_perecedero_descuento():
    p=ProductoPerecedero("X","A",100,2,dias_para_vencer=2)
    assert p.valor_total()==100.0
def test_perecedero_vencido():
    p=ProductoPerecedero("X","A",100,2,dias_para_vencer=0)
    assert p.valor_total()==0.0
def test_sistema_alertas():
    s=SistemaProductos(umbral_alerta=5)
    s.agregar_producto(Producto("A","A",10,2))
    assert len(s.verificar_alertas())==1
def test_valor_inventario():
    s=SistemaProductos(); s.agregar_producto(Producto("A","A",10,2))
    assert s.valor_total_inventario()==20.0
