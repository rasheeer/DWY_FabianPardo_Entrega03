from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('listarfull',views.listar_cliente_full),
    path('borrar_cliente/<str:rut>', views.borrar_cliente),
    path('editar_cliente/<str:rut>', views.editar_cliente),
    path('listar',views.listar_clientes),
    path('abogados',views.abogados),
    path('index',views.index),
    path('registrocliente',views.registro_cliente),
]
