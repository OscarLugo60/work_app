from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth import authenticate#, login, logout
#from django.http import HttpResponseRedirect
from .serializers import *
from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        RetrieveUpdateAPIView,
        DestroyAPIView,
    )
from rest_framework.views import APIView
from .models import Usuario

# Create your views here.

class APIUsuarioLogin(APIView):
    ### Vista para login ###

    ### Serializador para los campos de username y password ###
    serializer_class = LoginSerializer 

    def post(self, request):
        ### Carga los datos del serializador ###
        serializer = self.serializer_class(data=request.data)

        ### Verifica que los datos del serializador sean validos ###
        serializer.is_valid(raise_exception=True)

        ### Autentifica el usuario y clave, y almacena los datos en la variable usuario ###
        usuario = authenticate( 
            username = serializer.data.get('username'),
            password = request.data.get('password')
        )
        ###################################################################################

        if usuario:
            ### Si los datos fueron autenticados correctamente se retorna un codigo 200 y el token de dicho usuario ###
            token = Token.objects.get(user=usuario)
            return Response({'token':token.key}, status = status.HTTP_200_OK)
            ###########################################################################################################
        else:
            ### Si el usuario no existe en lugar del el token se envía un mensaje de error con el codigo 401 ###
            return Response({'error':'Usuario o contraseña errados'}, status = status.HTTP_401_UNAUTHORIZED)
            ####################################################################################################

class APIUsuarioActivo(ListAPIView):
    ### Vista para mostrar los datos del usuario activo ###
    serializer_class = UsuarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ### Implementando el token del usuario obtengo los datos del usuario y los devuelvo en una lista ###
        queryset = []
        queryset.append(Usuario.objects.get(id = self.request.user.id))
        ####################################################################################################
        return queryset

class UsuariosApiView(ListAPIView):
    ### Vista que genera el JSON para el listado de los usuarios ###
    serializer_class = UsuarioSerializer

    ### Paginado de 10 en 10 ###
    pagination_class = UsuarioPagination

    def get_queryset(self):
        ### Recibo un kword por url y filtro los usuario por nombre y apellido ###
        kword = self.request.query_params.get('kword', '')
        queryset = Usuario.objects.buscar_usuario(kword)
        return queryset
    
class UsuariosCreateApiView(CreateAPIView):
    ### Vista para crear usuarios ###
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioSerializerCreate

    def post(self, request):
        ### Sobrescribo el método post para implementar el manager de creación de usuarios ###
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = Usuario.objects.create_user(
            serializer.data.get('username'),
            serializer.data.get('nombre'),
            serializer.data.get('apellido'),
            serializer.data.get('departamento'),
            serializer.data.get('nivel'),
            serializer.data.get('password'),
        )
        return Response({'response':'Usuario creado correctamente'}, status = status.HTTP_200_OK)

class UsuarioUpdateApiView(RetrieveUpdateAPIView):
    ### Vista para actualizar los datos de los usuarios sin actualizar el campo de contraseña ###
    serializer_class = UsuarioSerializerUpdate
    queryset = Usuario.objects.all()

class PasswordUpdateApiView(APIView):
    ### Vista para actualizar contraseñas ###
    serializer_class = PasswordSerializer

    def post(self, request, *args, **kwargs):
        ### Sobrescribo el método post para establecer la contraseña al usuario especificado ###

        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        ### Recibo la variable 'pk' desde la url y obtengo el usuario que posea ese id ###
        user = Usuario.objects.get(id=kwargs['pk'])

        ### Establezco la contraseña al usuario que obtuve ###
        user.set_password(serializer.validated_data['password1'])

        ### Guardo el cambio realizado ###
        user.save()

        return Response({'response':'Contraseña actualizada correctamente'}, status = status.HTTP_200_OK)

class DepartamentoCreateApiView(CreateAPIView):
    serializer_class = DepartamentoSerializer

class DepartamentoListApiView(ListAPIView):
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        queryset = Departamento.objects.all()
        return queryset