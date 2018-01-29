from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from convocatorias.views import ConvocatoriaDetailView, ConvocatoriaListView
from convocatorias.feeds import ÚltimasConvocatoriasFeed

from .views import FechasPasadasView, HomepageView

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', ÚltimasConvocatoriasFeed()),
    path('convocatorias/', ConvocatoriaListView.as_view(), name='convocatoria_list'),
    path('convocatorias/<slug:slug>', ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
    path('fechas-pasadas', FechasPasadasView.as_view(), name='fechas-pasadas'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', HomepageView.as_view(), name="homepage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
