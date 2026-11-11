"""Se implementan AMBAS opciones autorizadas: FBV y CBV. La URL usa CBV, la FBV queda como alternativa valida."""
from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import obtener_metricas_totales, cargar_datos

def vista_dashboard_agua(request):
    # FBV - Vista Basada en Funcion
    historial = cargar_datos(fuente="csv")  # puede ser "csv", "json" o "dict"
    metricas = obtener_metricas_totales(historial)
    contexto = {"costo_total": metricas["costo_total_global"], "planta_critica": metricas["planta_mayor_consumo"], "lista_registros": historial}
    return render(request, "auditoria/dashboard.html", contexto)

class DashboardAguaView(TemplateView):
    # CBV - Vista Basada en Clase
    template_name = "auditoria/dashboard.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        historial = cargar_datos(fuente="csv")
        metricas = obtener_metricas_totales(historial)
        ctx.update({"costo_total": metricas["costo_total_global"], "planta_critica": metricas["planta_mayor_consumo"], "lista_registros": historial})
        return ctx
