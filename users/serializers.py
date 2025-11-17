from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    platform = serializers.IntegerField(help_text="ID numérico de la plataforma donde quiere iniciar sesión")