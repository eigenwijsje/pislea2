from django.contrib.syndication.views import Feed

from .models import Plan


class ÚltimosPlanesFeed(Feed):
    title = 'Últimos Planes Institucionales '
    link = ''
    description = ''

    def items(self):
        return Plan.objects.filter(estatus=7)

    def item_title(self, item):
        return item.entidad

    def item_description(self, item):
        return item.comentarios
