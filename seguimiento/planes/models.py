from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Plan(models.Model):
    ESTATUS_CHOICES = (
        (1, "Nuevo"),
        (2, "Plan requiere documento para su revisión"),
        (3, "Documento requiere revisión"),
        (4, "Documento en revisión"),
        (5, "Documento ha sido revisado")
    )
    entidad = models.CharField("Entidad", max_length=255)
    fuente = models.URLField("fuente", max_length=255)
    estatus = models.SmallIntegerField("Estatus", choices=ESTATUS_CHOICES, default=1)
    documento = models.FileField("Documento", blank=True, upload_to='files')
    publicado = models.DateField("Fecha de publicación")
    revisado = models.DateTimeField("Fecha de revisión", blank=True, null=True)
    revisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='planes',
                                verbose_name="Revisor")
    comentarios = models.TextField("Comentarios de la revisión", blank=True, null=True)

    class Meta:
        get_latest_by = 'publicado'
        ordering = ['-publicado']
        verbose_name = "Plan de Implementación"
        verbose_name_plural = "Planes de Implementación"

    def __str__(self):
        return self.entidad

    def get_absolute_url(self):
        return reverse('plan_detail', args=[str(self.pk)])
