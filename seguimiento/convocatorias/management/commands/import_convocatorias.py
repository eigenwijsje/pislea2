from django.core.management.base import BaseCommand
from django.db import IntegrityError

from convocatorias.models import Convocatoria

import json
from datetime import datetime


class Command(BaseCommand):
    help = 'Importa las convocatorias encontradas por la araña en infosicoes'

    def add_arguments(self, parser):
        parser.add_argument('convocatorias.json', type=str)

    def handle(self, *args, **options):
        with open(options['convocatorias.json']) as f:
            convocatorias = json.load(f)

        counts = [0, 0]
        for convocatoria in convocatorias:
            try:
                instance = Convocatoria(departamento=convocatoria['departamento'],
                                        entidad=convocatoria['entidad'],
                                        slug=convocatoria['cuce'],
                                        objeto=convocatoria['objeto'],
                                        tipo=convocatoria['tipo'],
                                        modalidad=convocatoria['modalidad'],
                                        añadida=datetime.now(),
                                        publicada=convocatoria['publicada'],
                                        presentada=convocatoria['presentada'],
                                        monto_bob=convocatoria['monto_bob'],
                                        monto_usd=convocatoria['monto_usd'],
                                        monto_eur=convocatoria['monto_eur'],
                                        contacto=convocatoria['contacto'],
                                        arch=convocatoria['arch'])
                instance.save()
            except IntegrityError:
                counts[0] += 1
            else:
                counts[1] += 1

        self.stdout.write(self.style.NOTICE('%s convocatorias ya estaban en el sistema ' % counts[0]))
        self.stdout.write(self.style.SUCCESS('%s convocatorias introducidas al sistema ' % counts[1]))