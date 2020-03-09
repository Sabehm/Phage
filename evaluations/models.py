from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save

EVALUATION_CHOICES = [
    ("A", "Activa"),
    ("P", "En Pausa"),
    ("F", "Finalizada")
]

# Create your models here.
class Evaluation(models.Model):
    """"
        docstring for EvaluationModel.
    La clase 'Evaluation' está compuesta por los siguientes parámetros y además funge como clase padre de la clase 'Device',
    con una relación 'Foreignkey'."""
    id_evaluation   = models.CharField(verbose_name='Evaluación', max_length=20, primary_key=True)
    start_date      = models.DateField(verbose_name='Fecha de Inicio', auto_now_add=True)
    end_date        = models.DateField(verbose_name='Fecha de Término', null=True, blank=True)
    status          = models.CharField(verbose_name='Estado', max_length=1, choices=EVALUATION_CHOICES)
    username        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug            = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['id_evaluation']

    def __str__(self):
        return self.id_evaluation


class Device(models.Model):
    """docstring for DeviceModel."""
    id_device = models.CharField(verbose_name='Dispositivo', max_length=20, primary_key=True)
    name = models.CharField(verbose_name='Nombre', max_length=50)
    processor = models.TextField(verbose_name='Procesador')
    internal_storage = models.CharField(verbose_name='Almacenamiento Interno', max_length=10)
    ram = models.CharField(verbose_name='RAM', max_length=10)
    os = models.CharField(verbose_name='Sistema Operativo', max_length=30)
    eth = models.CharField(verbose_name='Ethernet', max_length=100, null=True, blank=True)
    wifi = models.CharField(verbose_name='Wi-Fi', max_length=100, null=True, blank=True)
    id_evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        ordering = ['id_device']

    def __str__(self):
        return self.id_device


class DeviceStatus(models.Model):
    """docstring for EstadoDispositivoModel."""
    id_device = models.OneToOneField(Device, related_name='status', on_delete=models.CASCADE)
    is_infected = models.BooleanField()
    is_vulnerated = models.BooleanField()

    class Meta:
        verbose_name = 'Estado del dipositivo'
        verbose_name_plural = 'Estado del dispositivo'
        ordering = ['is_vulnerated', 'id_device']

    def __str__(self):
        return '%s' % (self.id_device)

def pre_save_evaluation_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.id_evaluation)

pre_save.connect(pre_save_evaluation_receiver, sender=Evaluation)
