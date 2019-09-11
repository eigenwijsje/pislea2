from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import IntegrityError

import json
import os

import requests

from planes.models import Plan


class Command(BaseCommand):
    help = 'Importa los planes encontrados por el reastreador'

    def add_arguments(self, parser):
        parser.add_argument('planes', type=str)

    def handle(self, *args, **options):
        with open(options['planes']) as f:
            planes = json.load(f)

        counts = [0, 0]

        for plan in planes:
            response = requests.get(plan['fuente'])
            if response.status_code == 404:
                self.stderr.write(self.style.ERROR('{}: error 404'.format(plan['fuente'])))
            else:
                filename = response.headers['Content-Disposition'].split()[2][10:-1]

                with open(filename, 'wb') as f:
                    f.write(response.content)

            instance = Plan(entidad=plan['entidad'], fuente=plan['fuente'])

            try:
                instance.save()
                if filename:
                    with open(filename, 'rb') as f:
                        instance.documento.save(filename, File(f))
                        os.remove(filename)
            except IntegrityError:
                counts[0] += 1
            else:
                counts[1] += 1

        self.stdout.write(self.style.NOTICE('{} planes ya estaban en el sistema'.format(counts[0])))
        self.stdout.write(self.style.SUCCESS('{} planes introducidos al sistema'.format(counts[1])))
