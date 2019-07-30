from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['fechas-pasadas', 'proxima-fecha', 'homepage']

    def location(self, obj):
        return reverse(obj)

