from convocatorias.models import Convocatoria
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Elimina los documentos base de contratación que están libres de software privativo'

    def handle(self, *args, **options):
        convocatorias = Convocatoria.objects.filter(estatus=6)
        count = 0

        for convocatoria in convocatorias:
            if bool(convocatoria.documento):
                convocatoria.documento.delete()
                count += 1

        if count > 0:
            self.stdout.write(self.style.SUCCESS('%i documentos eliminados' % count))
