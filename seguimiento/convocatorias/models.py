from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Convocatoria(models.Model):
    STATUS_CHOICES = (
        (1, "Nueva"),
        (2, "Convocatoria no necesita revisión"),
        (3, "Convocatoria requiere documento para su revisión"),
        (4, "Documento requiere revisión"),
        (5, "Documento en revisión"),
        (6, "Convocatoria libre de software privativo"),
        (7, "Convocatoria contaminada con software privativo")
    )
    departamento = models.CharField("Departamento", max_length=16)
    entidad = models.CharField("Entidad", max_length=255)
    slug = models.SlugField("CUCE", unique=True)
    objeto = models.CharField("Objeto", max_length=512)
    enlace = models.URLField(max_length=255)
    modalidad = models.CharField("Modalidad", max_length=64)
    tipo = models.CharField("Tipo", max_length=16)
    estatus = models.SmallIntegerField("Estatus", choices=STATUS_CHOICES, default=1)
    añadida = models.DateTimeField("Añadida")
    publicada = models.DateField("Fecha de publicación")
    presentada = models.DateField("Fecha de presentación")
    impugnada = models.DateField("Impugnada", blank=True, null=True)
    monto_bob = models.DecimalField("Monto Bs.", max_digits=16, decimal_places=2)
    monto_usd = models.DecimalField("Monto $us.", max_digits=16, decimal_places=2)
    monto_eur = models.DecimalField("Monto €", max_digits=16, decimal_places=2)
    contacto = models.CharField("Contacto", max_length=128)
    documento = models.FileField("D.B.C.", blank=True, upload_to='files')
    arch = models.CharField("D.B.C. Arch", editable=False, max_length=16)
    añadido = models.DateTimeField("D.B.C. añadido", blank=True, editable=False, null=True)
    revisado = models.DateTimeField("D.B.C. revisado", blank=True, null=True)
    revisor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='documentos',
                                verbose_name="Revisor")
    notas = models.TextField("Notas de la revisión", blank=True, null=True)

    class Meta:
        get_latest_by = 'añadida'
        ordering = ['-publicada']
        verbose_name = "Convocatoria"
        verbose_name_plural = "Convocatorias"

    def __str__(self):
        return self.objeto

    def get_absolute_url(self):
        return reverse('convocatoria_detail', args=[str(self.slug)])
