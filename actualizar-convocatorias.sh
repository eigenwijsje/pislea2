#!/bin/bash

# ajustar segun la necesidad
DIR_BASE=/directorio/donde/esta/pislea2

PYTHON_VENV=$DIR_BASE/venv/bin/python
SCRAPY=$DIR_BASE/venv/bin/scrapy

echo "ejecutando la aranya scrapy"
cd $DIR_BASE/infosicoes
# vaciando el json para evitar registros duplicados
# TODO: leer solo las convocatorias del dia de hoy
echo "" > ../seguimiento/convocatorias.json

$SCRAPY runspider infosicoes/spiders/convocatorias.py --nolog -o ../seguimiento/convocatorias.json
wc --lines ../seguimiento/convocatorias.json

#La aplicación Django requiere la configuración de la variable de entorno ``DJANGO_SETTINGS_MODULE``:
cd $DIR_BASE/seguimiento
export DJANGO_SETTINGS_MODULE=seguimiento.settings.local

echo "importando"
$PYTHON_VENV manage.py import_convocatorias convocatorias.json

exit 0

