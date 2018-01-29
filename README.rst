#####################################################################################################################################
Próxima fecha clave y seguimiento de la Comunidad de Software Libre al Plan de Implementación de Software Libre y Estándares Abiertos
#####################################################################################################################################

Esta aplicación facilita el seguimiento a las convocatorias nacionales para contrataciones de bienes y de servicios generales y de consultoría publicadas por el SICOES.

La información básica de todas las contrataciones se obtienen con un rastreador con Scrapy.

Esta información se revisa a través de una aplicación Django donde se determina si es necesario el documento base de contratación para su evaluación.

El documento base de contratación es obtenido a través de un comando de Django admin y evaluado manualmente por voluntarios de la Comunidad de Software Libre Bolivia.

La evaluación determina finalmente si la convocatoria está esta libre de o contaminada por software privativo.

Los resultados de la evaluación son publicados a través de el sitio Web.

Adicionalemte la aplicación muestra la próxima fecha clave en el `Plan de Implementación de Software Libre y Estándares Abiertos`_ de acuerdo al Decreto Supremo 3251 publicado por el Gobierno de Bolivia el 12 de julio de 2017.

==============
Requerimientos
==============

::

    Django==2.0.1
    requests==2.18.4
    Scrapy==1.5.0

======
Fechas
======

12 de agosto de 2017:
  La máximas autoridades ejecutivas de las entidades del sector público remitirán a la AGETIC la designación de la o las personas responsables de la coordinación de la implementación de los planes establecidos en el Artículo 6

12 de octubre de 2017:
  El Ente Rector del Gobierno Electrónico y Tecnología de Información y Comunicación establecerá los mecanismos y condiciones de accesso a los datos establecidos en el Artículo 4

12 de enero de 2018:
  El Ministerio de Obras Públicas, Servicios y Vivienda establecerá las condiciones de acceso gratuito a los portales señalados en el Artículo 3

12 de julio de 2018:
  Las Entidades Públicas enviarán a la AGETIC el Plan Institucional de Implementación de Gobierno Electrónico aprobado por la Máxima Autoridad Ejecutiva, para su validación, seguimineto de su aplicación y publicación en su página web

12 de enero de 2019:
  Las Entidades Públicas enviaran a la AGETIC el plan Institucional de Implementación de Software Libre y Estandares Abiertos aprobado por la Máxima Autoridad Ejecutiva, para su validación, seguimineto de su aplicación y publicación en su página web

12 de julio de 2021:
  La AGETIC en coordinación con las entidades del sector público realizarán la evaluacion al proceso de implementación de Software Libre y Estandares Libres, para considerar el estado de la situación y el nivel de cumplimiento de los aspectos técnicos, financieros administrativos y normativos a efectuar los ajustes necesarios, producto de la evaluación

6 meses desde la aprobación de le Resolución Ministerial emitida por el Ministerio de Obras Públicas, Servicios y Vivienda sobre las condiciones de acceso gratuitos establecidos en la Disposicion Transitoria Tercera:
  El Comité Plurinacional de Tecnologías de Información y Comunicación a) aprobará los criterios de elegibilidad para los sitios web establecidos en el Paragafo II del Articulo 3. b) determinará y remitirá la lista de sitios web a la Autoridad de Regulación y Fizcalización de Telecomunicaciones y Transporte, para su verficación y cumplimento

Las fechas están descritas en ``fechas.json``.

.. _Plan de Implementación de Software Libre y Estándares Abiertos: https://www.agetic.gob.bo/#/plan-de-implementacion-de-software-libre-y-estandares-abiertos
