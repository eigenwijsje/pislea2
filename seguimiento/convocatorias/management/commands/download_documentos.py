from datetime import datetime
import os

import requests
from convocatorias.models import Convocatoria
from django.core.files import File
from django.core.management.base import BaseCommand

URL = 'https://www.infosicoes.com/contenido/paginas/procesos/archivo.php'


class Command(BaseCommand):
    help = 'Descarga los documentos base de contratación requeridos para ser evaluados'

    def handle(self, *args, **options):
        convocatorias = Convocatoria.objects.filter(estatus=3)  # Requiere documento para su revisión

        count = 0
        for convocatoria in convocatorias:
            response = requests.post(URL, data={'arch': convocatoria.arch})
            if response.url == 'https://www.infosicoes.com/limite-de-descargas-excedido.html':
                self.stderr.write(self.style.ERROR('Limite de descargas excedido!'))
                break
            if response.ok:
                filename = response.headers['Content-Disposition'][21:-1]
                with open(filename, 'wb') as f:
                    f.write(response.content)

                with open(filename, 'rb') as f:
                    convocatoria.documento.save(filename, File(f))

                os.remove(filename)
                count += 1

                convocatoria.añadido = datetime.now()
                convocatoria.estatus = 4  # Documento requiere revisión
                convocatoria.save()

        if count > 0:
            self.stdout.write(self.style.SUCCESS('%i documentos descargados' % count))

