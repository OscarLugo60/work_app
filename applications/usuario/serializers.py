from rest_framework import serializers, pagination
from .models import Usuario, Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = (
            'id',
            'nombre'
        )

class UsuarioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'nombre',
            'apellido',
            'departamento',
            'get_nivel_display',
            'get_estatus_display'
        )

class UsuarioPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 20

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UsuarioSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'nombre',
            'apellido',
            'departamento',
            'nivel',
            'password',
        )

class UsuarioSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'nombre',
            'apellido',
            'departamento',
            'nivel',
        )

class PasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        
        return data