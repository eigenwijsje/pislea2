from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import views
from django.urls import path, include
from django.views.decorators.cache import cache_page

from convocatorias.feeds import ÚltimasConvocatoriasFeed
from convocatorias.sitemaps import ConvocatoriaSitemap
from convocatorias.views import ConvocatoriaDetailView, ConvocatoriaListView
from planes.views import PlanDetailView, PlanListView
from .sitemaps import StaticViewSitemap
from .views import FechasPasadasView, HomepageView, PróximaFechaView

admin.autodiscover()

sitemaps = {
    'convocatorias': ConvocatoriaSitemap,
    'flatpages': FlatPageSitemap,
    'static': StaticViewSitemap,
}

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
                  path('sitemap.xml', cache_page(86400)(views.index), {'sitemaps': sitemaps}),
                  path('sitemap-<section>.xml', cache_page(86400)(views.sitemap), {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
