from django.contrib.sitemaps import Sitemap

from convocatorias.models import Convocatoria


class ConvocatoriaSitemap(Sitemap):
    changefreq = 'yearly'

    def items(self):
        return Convocatoria.objects.filter(estatus__in=[7, 8])

    def lastmod(self, obj):
        return obj.añadido
