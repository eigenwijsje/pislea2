from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Plan(models.Model):
    ESTATUS_CHOICES = (
        (1, "Documento requiere revisión"),
        (2, "Documento ha sido revisado")
    )
    entidad = models.CharField("Entidad", max_length=255, unique=True)
    fuente = models.URLField("Fuente", max_length=255)
    estatus = models.SmallIntegerField("Estatus", choices=ESTATUS_CHOICES, default=1)
    documento = models.FileField("Documento", upload_to='planes')
    recibido = models.DateField("Fecha de recepción", blank=True, null=True)
    publicado = models.DateField("Fecha de publicación", blank=True, null=True)
    revisado = models.DateField("Fecha de revisión", blank=True, null=True)
    revisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='planes',
                                verbose_name="Revisor")
    comentarios = models.TextField("Comentarios de la revisión", blank=True, null=True)
    páginas = models.IntegerField("Páginas en total", default=0)
    páginas_quitadas = models.CharField("Páginas quitadas", blank=True, max_length=64, null=True)

    class Meta:
        get_latest_by = 'recibido'
        ordering = ['entidad']
        verbose_name = "Plan de Implementación"
        verbose_name_plural = "Planes de Implementación"

    def __str__(self):
        return self.entidad

    def get_absolute_url(self):
        return reverse('plan_detail', args=[str(self.pk)])

    @property
    def días_de_retraso(self):
        if self.recibido > settings.PLAZO_PLANES:
            return '{} días de retraso'.format((self.recibido - settings.PLAZO_PLANES).days)
        else:
            return None

    @property
    def días_después(self):
        return '{} días después'.format((self.publicado - self.recibido).days)
