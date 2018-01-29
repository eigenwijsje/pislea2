from django.views.generic import TemplateView

import json
from datetime import datetime


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        proxima_fecha = None

        with open('fechas.json', 'r') as f:
            fechas = json.loads(f.read())
            for fecha in fechas:
                try:
                    hasta = datetime.strptime(fecha['hasta'], '%Y-%m-%d')
                except ValueError:
                    pass
                else:
                    quien = fecha['quien']
                    que = fecha['que']

                    if proxima_fecha is None:
                        if hasta > datetime.today():
                            proxima_fecha = dict(hasta=hasta, quien=quien, que=que)
                    elif hasta == proxima_fecha['hasta']:
                        proxima_fecha['quien2'] = fecha['quien']
                        proxima_fecha['que2'] = fecha['que']

        context['hace_dias'] = (datetime.today() - datetime(2017, 7, 12)).days
        context['en_dias'] = (proxima_fecha['hasta'] - datetime.today()).days
        context['quien'] = proxima_fecha['quien']
        context['que'] = proxima_fecha['que']
        context['quien2'] = proxima_fecha.get('quien2')
        context['que2'] = proxima_fecha.get('que2')

        return context


class FechasPasadasView(TemplateView):
    template_name = 'fechas_pasadas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fechas_pasadas = []
        with open('fechas.json', 'r') as f:
            fechas = json.loads(f.read())
            for fecha in fechas:
                try:
                    hasta = datetime.strptime(fecha['hasta'], '%Y-%m-%d')
                except ValueError:
                    pass
                else:
                    quien = fecha['quien']
                    que = fecha['que']
                if hasta < datetime.now():
                    fechas_pasadas.append(dict(hasta=hasta, quien=quien, que=que))

        context['fechas_pasadas'] = fechas_pasadas

        return context
