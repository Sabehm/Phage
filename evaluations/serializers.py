from .models import Evaluation, Device, DeviceStatus
from rest_framework import serializers

class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = ['is_infected', 'is_vulnerated']

class DeviceSerializer(serializers.ModelSerializer):
    status = DeviceStatusSerializer(read_only=True)
    class Meta:
        model = Device
        fields = ['id_device', 'name', 'processor', 'internal_storage', 'ram', 'os', 'eth', 'wifi', 'id_evaluation', 'status']

class EvaluationSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    class Meta:
        model = Evaluation
        fields = ['id_evaluation', 'start_date', 'end_date', 'status', 'devices']
