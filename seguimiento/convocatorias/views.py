from django.views.generic import DetailView, ListView
from rest_framework import viewsets

from .models import Convocatoria
from .serializers import ConvocatoriaSerializer


class ConvocatoriaView(object):
    model = Convocatoria


class ConvocatoriaListView(ConvocatoriaView, ListView):
    paginate_by = 10

    def get_queryset(self):
        if 'ejemplares' in self.request.GET:
            queryset = Convocatoria.objects.filter(estatus=8)
        else:
            queryset = Convocatoria.objects.filter(estatus=7)

        return queryset


class ConvocatoriaDetailView(ConvocatoriaView, DetailView):
    queryset = Convocatoria.objects.filter(estatus__in=[7, 8])


class ConvocatoriaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Convocatoria.objects.filter(estatus__in=[7, 8])
    serializer_class = ConvocatoriaSerializer

    def get_queryset(self):
        queryset = Convocatoria.objects.filter(estatus__in=[7, 8])

        entidad = self.request.query_params.get('entidad', None)
        estatus = self.request.query_params.get('estatus', None)
        departamento = self.request.query_params.get('departamento', None)

        if entidad:
            queryset = queryset.filter(entidad=entidad)
        if estatus:
            queryset = queryset.filter(estatus=estatus)
        if departamento:
            queryset = queryset.filter(departamento=departamento)

        return queryset
