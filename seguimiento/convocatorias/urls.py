from django.urls import path

from .views import ConvocatoriaDetailView, ConvocatoriaListView

urlpatterns = [
    path('convocatorias/', ConvocatoriaListView.as_view(), name='convocatoria_list'),
    path('convocatorias/<slug:slug>', ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
]
