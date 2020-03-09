from django.contrib import admin
from .models import Evaluation, Device, DeviceStatus

# Register your models here.

admin.site.register(Evaluation)
admin.site.register(Device)
admin.site.register(DeviceStatus)