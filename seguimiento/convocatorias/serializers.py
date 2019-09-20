from rest_framework import serializers

from .models import Convocatoria


class ConvocatoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = ['url', 'entidad', 'departamento', 'slug', 'objeto', 'modalidad', 'tipo', 'estatus', 'notas']
        model = Convocatoria
