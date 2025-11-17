from rest_framework import serializers
from .models import Device
import ipaddress

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'ip_address', 'active']
        read_only_fields = ['id']

 # VALIDACIÓN A: verificar que la IP sea válida
    def validate_ip_address(self, value):
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise serializers.ValidationError("Invalid IP address format.")
        return value