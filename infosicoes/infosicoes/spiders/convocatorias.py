import scrapy

from datetime import datetime
from urllib.parse import quote

BASE_URL = 'https://www.infosicoes.com'


class ConvcatoriasSpider(scrapy.Spider):
    name = 'convocatorias'
    allowed_domains = ['infosicoes.com']
    start_urls = [
        'https://www.infosicoes.com/contrataciones-de-bienes-bolivia.html',
        'https://www.infosicoes.com/contrataciones-de-consultoria-bolivia.html',
        'https://www.infosicoes.com/contrataciones-de-ser-generales-bolivia.html',
    ]

    def parse(self, response):
        for convocatoria in response.css('table > tr'):
            departamento = convocatoria.css('td.celda-entidad > a::text').extract_first()
            entidad = convocatoria.css('td.celda-entidad > h4 > a::text').extract_first()
            cuce = convocatoria.css('td.celda-entidad > b > a::text').extract_first()

            if not cuce:
                continue

            objeto = convocatoria.css('td.celda-objeto > h2 > a::text').extract_first()
            enlace = quote(convocatoria.css('td.celda-objeto > h2 > a::attr(href)').extract_first().replace('\\r\\n', ''), safe=':/')

            tipo, modalidad = map(str.strip, convocatoria.css('td.celda-objeto::text').extract()[1].split('-'))
            estado, publicada, presentada = list(map(str.strip, convocatoria.css('td.celda-estado::text').extract()))
            publicada = datetime.strptime(publicada.split(':')[1].strip(), '%d-%m-%Y').date()
            presentada = datetime.strptime(presentada.split(':')[1].strip(), '%d-%m-%Y').date()
            monto_bob, monto_usd, monto_eur = list(map(str.strip, convocatoria.css('td.celda-monto::text').extract()))
            monto_bob = float(monto_bob.split(' ')[0].replace('.', '').replace(',', '.'))
            monto_usd = float(monto_usd.split(' ')[0].replace('.', '').replace(',', '.'))
            monto_eur = float(monto_eur.split(' ')[0].replace('.', '').replace(',', '.'))
            contacto = convocatoria.css('td.celda-contacto::text').extract_first()
            documentos = convocatoria.css('td.celda-archivos > form > button::text').extract()
            arch = convocatoria.css('td.celda-archivos > form > input::attr(value)').extract()

            for n in range(len(documentos)):
                if documentos[n] == 'D.B.C.':
                    dbc_arch = arch[n]

            if cuce:
                yield dict(
                    departamento=departamento,
                    entidad=entidad,
                    cuce=cuce,
                    objeto=objeto,
                    enlace="%s/%s" % (BASE_URL, enlace),
                    tipo=tipo,
                    modalidad=modalidad,
                    publicada=publicada,
                    presentada=presentada,
                    monto_bob=monto_bob,
                    monto_usd=monto_usd,
                    monto_eur=monto_eur,
                    contacto=contacto,
                    arch=dbc_arch)

            current = response.css('div.box_generador > a.box_generador_espacio_actual::attr(href)').extract_first()
            other_pages = response.css('div.box_generador > a.box_generador_espacio::attr(href)').extract()

            for page in other_pages:
                if page is not current:
                    next_page = response.urljoin(page)
                    yield scrapy.Request(next_page, callback=self.parse)
