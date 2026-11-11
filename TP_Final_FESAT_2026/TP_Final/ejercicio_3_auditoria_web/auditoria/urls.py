from django.urls import path
from .views import vista_dashboard_agua, DashboardAguaView
urlpatterns = [
    path("agua/dashboard/", DashboardAguaView.as_view(), name="dashboard_agua"),
    path("agua/dashboard-fbv/", vista_dashboard_agua, name="dashboard_agua_fbv"),
]
