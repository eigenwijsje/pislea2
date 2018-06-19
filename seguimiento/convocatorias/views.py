from django.views.generic import DetailView, ListView
from django.db.models import Q

from .models import Convocatoria


class ConvocatoriaView(object):
    model = Convocatoria
    queryset = Convocatoria.objects.filter(Q(estatus=7) | Q(estatus=8))


class ConvocatoriaListView(ConvocatoriaView, ListView):
    def get_queryset(self):
        if 'ejemplares' in self.request.GET:
            queryset = Convocatoria.objects.filter(estatus=8)
        else:
            queryset = Convocatoria.objects.filter(estatus=7)

        return queryset


class ConvocatoriaDetailView(ConvocatoriaView, DetailView):
    pass
