from django.views.generic import DetailView, ListView
from .models import Convocatoria


class ConvocatoriaView(object):
    model = Convocatoria
    queryset = Convocatoria.objects.filter(estatus=7)


class ConvocatoriaListView(ConvocatoriaView, ListView):
    pass


class ConvocatoriaDetailView(ConvocatoriaView, DetailView):
    pass
