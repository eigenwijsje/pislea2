from django.views.generic import DetailView, ListView
from django.conf import settings
from .models import Plan


class PlanView(object):
    model = Plan
    queryset = Plan.objects.all()


class PlanListView(PlanView, ListView):
    paginate_by = 10


class PlanDetailView(PlanView, DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plan = self.get_object()

        context['card_title'] = 'Plan de Implementación de Software Libre y Estándares Abiertos'

        if plan.recibido > settings.PLAZO_PLANES:
            context['card_description'] = \
                'El PISLEA de {entidad} fue recibido por la AGETIC con {días_de_retraso} y fue publicado {días_después}'.format(
                    entidad=plan.entidad, días_de_retraso=plan.días_de_retraso, días_después=plan.días_después)
        else:
            context['card_description'] = \
                'El PISLEA de {entidad} fue recibido por la AGETIC dentro del plazo y fue publicado {días_después}'.format(
                    entidad=plan.entidad, días_después=plan.días_después)

        return context
