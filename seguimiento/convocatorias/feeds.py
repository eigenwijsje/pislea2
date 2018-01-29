from django.contrib.syndication.views import Feed
from .models import Convocatoria


class ÚltimasConvocatoriasFeed(Feed):
    title = ''
    link = ''
    description = ''

    def items(self):
        return Convocatoria.objects.filter(estatus=7)

    def item_title(self, item):
        return '%s - %s: %s' % (item.departmento, item.entidad, item.objeto)

    def item_description(self, item):
        return item.notas

