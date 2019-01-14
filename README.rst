###############################################################################################################
Seguimiento de la Comunidad de Software Libre al Plan de Implementación de Software Libre y Estándares Abiertos
###############################################################################################################

Esta aplicación facilita el seguimiento a las convocatorias nacionales para contrataciones de bienes, de servicios generales y de consultorías, publicadas por el SICOES_, a través del sitio de INFOSICOES_.

La información básica de todas las contrataciones se obtienen con un rastreador con Scrapy_.

Esta información se revisa a través de una aplicación Django_, donde se determina si es necesario el documento base de contratación para su evaluación.

El documento base de contratación es obtenido a través de un comando de Django y evaluado manualmente por voluntarios de la Comunidad de Software Libre Bolivia.

La evaluación determina finalmente si la convocatoria está esta libre de o contaminada por software privativo.

Los resultados de la evaluación son publicados a través de el sitio Web.

Esta aplicación también facilita el seguimiento y revisión de los Planes Instituionales de Implementación de Software Libre y Estandares Abiertos publicados en el sitio de la AGETIC_ a partir del 12 de enerode 2019.
 
Adicionalmente la aplicación muestra la próxima fecha clave en el `Plan de Implementación de Software Libre y Estándares Abiertos`_ de acuerdo al Decreto Supremo 3251 publicado por el Gobierno de Bolivia el 12 de julio de 2017.

==============
Requerimientos
==============

::

    Django==2.0.5
    requests==2.18.4
    Scrapy==1.5.0

===========
Instalación
===========

Crear inicialmente y activar un entorno virtual que albergue a los requerimientos del proyecto.

::

    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements/base.txt

=========
Ejecución
=========

Una vez activado en entorno virtual, se puede ejecutar el rastreador, dentro del subdirectorio ``infosicoes``:

::

    (venv) $ scrapy runspider convocatorias.py --nolog -o ../seguimiento/convocatorias.json

La aplicación Django requiere la configuración de la variable de entorno ``DJANGO_SETTINGS_MODULE``:

::

    (venv) $ export DJANGO_SETTINGS_MODULE=seguimiento.settings.local

Para empezar: crear la base de datos y crear un super usuario, dentro del subirectorio ``seguimiento``:

::

    (venv) $ ./manage.py migrate
    (venv) $ ./manage.py createsuperuser

Luego se pueden importar los resultados del rastreador:

::

    (venv) $ ./manage.py import_convocatorias convocatorias.json

Y para ejecutar la aplicación:

::

    (venv) $ ./manage.py runserver

Luego de marcar, en la interfaz de administración, convocatorias que necesiten del documento base de contratación para su evaluación, se puede descargar los documentos:

::

    (venv) $ ./manage.py download_documentos

Finalmente, una vez más en la interfaz de administración, se puede acceder a las convocatorias nuevamente y los documentos estarán disponibles.

======
Fechas
======

12 de agosto de 2017:
  La máximas autoridades ejecutivas de las entidades del sector público debían remitir a la AGETIC la designación de la o las personas responsables de la coordinación de la implementación de los planes establecidos en el Artículo 6

12 de octubre de 2017:
  El Ente Rector del Gobierno Electrónico y Tecnología de Información y Comunicación debían establecer los mecanismos y condiciones de accesso a los datos establecidos en el Artículo 4

12 de enero de 2018:
  El Ministerio de Obras Públicas, Servicios y Vivienda debía establecer las condiciones de acceso gratuito a los portales señalados en el Artículo 3

12 de julio de 2018:
  Las Entidades Públicas deben enviar a la AGETIC el Plan Institucional de Implementación de Gobierno Electrónico aprobado por la Máxima Autoridad Ejecutiva, para su validación, seguimineto de su aplicación y publicación en su página web

12 de enero de 2019:
  Las Entidades Públicas deben enviar a la AGETIC el plan Institucional de Implementación de Software Libre y Estandares Abiertos aprobado por la Máxima Autoridad Ejecutiva, para su validación, seguimineto de su aplicación y publicación en su página web

12 de julio de 2021:
  La AGETIC en coordinación con las entidades del sector público deben realizar la evaluacion al proceso de implementación de Software Libre y Estandares Libres, para considerar el estado de la situación y el nivel de cumplimiento de los aspectos técnicos, financieros administrativos y normativos a efectuar los ajustes necesarios, producto de la evaluación

6 meses desde la aprobación de le Resolución Ministerial emitida por el Ministerio de Obras Públicas, Servicios y Vivienda sobre las condiciones de acceso gratuitos establecidos en la Disposicion Transitoria Tercera:
  El Comité Plurinacional de Tecnologías de Información y Comunicación a) deben aprobar los criterios de elegibilidad para los sitios web establecidos en el Paragafo II del Articulo 3. b) deben determinar y remitirá la lista de sitios web a la Autoridad de Regulación y Fizcalización de Telecomunicaciones y Transporte, para su verficación y cumplimento

Las fechas están descritas en ``fechas.json``.

.. _Plan de Implementación de Software Libre y Estándares Abiertos: https://www.agetic.gob.bo/#/plan-de-implementacion-de-software-libre-y-estandares-abiertos
.. _Scrapy: https://scrapy.org/
.. _Django: http://djangoproject.com/
.. _SICOES: https://www.sicoes.gob.bo/
.. _INFOSICOES: https://www.infosicoes.com/
.. _AGETIC: https://agetic.gob.bo/
