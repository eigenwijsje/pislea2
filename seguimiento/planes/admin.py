from django.contrib import admin
from django.utils.html import format_html

from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('entidad', 'enlace_fuente', 'estatus', 'documento', 'comentarios')
        }),
        ('Fechas', {
            'fields': ('recibido', 'publicado', 'revisado')
        }),
        ('Páginas', {
            'fields': ('páginas', 'páginas_quitadas')
        })
    )
    list_display = ('entidad', 'recibido', 'publicado')
    list_filter = ('estatus',)
    readonly_fields = ['entidad', 'enlace_fuente', 'documento']

    def enlace_fuente(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.fuente)
