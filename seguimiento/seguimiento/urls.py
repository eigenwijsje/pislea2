from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from convocatorias.feeds import ÚltimasConvocatoriasFeed
from convocatorias.views import ConvocatoriaDetailView, ConvocatoriaListView
from planes.views import PlanDetailView, PlanListView
from .views import FechasPasadasView, HomepageView, PróximaFechaView

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convocatorias/feed', ÚltimasConvocatoriasFeed()),
    path('convocatorias/', ConvocatoriaListView.as_view(), name='convocatoria-list'),
    path('convocatorias/<slug:slug>', ConvocatoriaDetailView.as_view(), name='convocatoria-detail'),
    path('planes/', PlanListView.as_view(), name='plan-list'),
    path('planes/<int:pk>', PlanDetailView.as_view(), name='plan-detail'),
    path('fechas-pasadas', FechasPasadasView.as_view(), name='fechas-pasadas'),
    path('proxima-fecha', PróximaFechaView.as_view(), name='proxima-fecha'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', HomepageView.as_view(), name="homepage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
