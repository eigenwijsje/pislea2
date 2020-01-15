from django.views.generic import TemplateView

import json
from datetime import datetime

from planes.models import Plan


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open('fechas.json', 'r') as f:
            fechas = json.loads(f.read())

        context['años'], dias = divmod((datetime.today() - datetime(2017, 7, 11)).days, 365)
        context['meses'], context['dias'] = divmod(dias, 30)
        context['años2'], días2 = divmod((datetime.today() - datetime(2019, 1, 12)).days, 365)
        context['meses2'], context['días2'] = divmod(días2, 30)
        context['quien'] = fechas[4]['quien']
        context['que'] = fechas[4]['que']
        context['publicados'] = Plan.objects.all().count()

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


class PróximaFechaView(TemplateView):
    template_name = 'proxima_fecha.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                if hasta > datetime.now():
                    en_días = (hasta - datetime.today()).days
                    context['proxima_fecha'] = dict(en_dias=en_días, hasta=hasta, quien=quien, que=que)
                    break

            return context
