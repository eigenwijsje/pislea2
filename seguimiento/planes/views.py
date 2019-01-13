from django.views.generic import DetailView, ListView

from .models import Plan


class PlanView(object):
    model = Plan
    queryset = Plan.objects.all()


class PlanListView(PlanView, ListView):
    pass


class PlanDetailView(PlanView, DetailView):
    pass
