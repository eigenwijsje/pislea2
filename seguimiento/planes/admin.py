from django.contrib import admin
from django.utils.html import format_html

from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('entidad', 'publicado', 'revisado', 'estatus')
    list_filter = ('estatus',)

    def enlace_origen(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.origen)
