from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('api/', views.API_objets.as_view()),
    path('api/<int:pk>/', views.API_objets_details.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('', views.index),
    path('listarfull',views.listar_cliente_full),
    path('borrar_cliente/<str:rut>', views.borrar_cliente),
    path('editar_cliente/<str:rut>', views.editar_cliente),
    path('listar',views.listar_clientes),
    path('abogados',views.abogados),
    path('index',views.index),
    path('registrocliente',views.registro_cliente),
    path('filtros',views.filtros),
]
