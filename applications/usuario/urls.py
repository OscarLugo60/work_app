from django.urls import path

from . import views

app_name = "usuario_app"

urlpatterns = [
    path(
        'api/lista-usuarios/',
        views.UsuariosApiView.as_view(),
        name='api-lista-usuarios',
    ),
    path(
        'api/login/',
        views.APIUsuarioLogin.as_view(),
        name='api-login',
    ),
    path(
        'api/crear-usuario/',
        views.UsuariosCreateApiView.as_view(),
        name='api-crear-usuario',
    ),
    path(
        'api/actualizar-usuario/<pk>',
        views.UsuarioUpdateApiView.as_view(),
        name='api-actualizar-usuario'
    ),
    path(
        'api/actualizar-password/<pk>',
        views.PasswordUpdateApiView.as_view(),
        name='api-actualizar-password'
    ),
    path(
        'api/usuario-activo/',
        views.APIUsuarioActivo.as_view(),
        name='api-usuario-activo',
    ),
    path(
        'api/crear-departamento/',
        views.DepartamentoCreateApiView.as_view(),
        name='api-crear-departamento',
    ),
    path(
        'api/lista-departamentos/',
        views.DepartamentoListApiView.as_view(),
        name='api-lista-departamentos',
    ),
]