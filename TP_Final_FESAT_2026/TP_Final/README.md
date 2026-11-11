# TP Final Integrador - Python FESAT 2026
## Estructura
- `ejercicio_1_sensores/` - Funciones puras, sanitizacion y resumen
- `ejercicio_2_productos/` - POO: Producto, Inventario, Sistema
- `ejercicio_3_auditoria_web/` - Proyecto Django + pytest + dashboard

## Entrega
Repositorio publico GitHub o ZIP. Sin .venv, sin __pycache__, sin .pytest_cache

## Como correr
### Ej 1
```
cd ejercicio_1_sensores
python main.py
pytest -v
```
### Ej 2
```
cd ejercicio_2_productos
python main.py
pytest -v
```
### Ej 3
```
cd ejercicio_3_auditoria_web
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# http://127.0.0.1:8000/agua/dashboard/
pytest -v
```
