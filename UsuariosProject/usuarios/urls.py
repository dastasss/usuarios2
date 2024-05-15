from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('<int:id>/', views.detalle_usuario, name='detalle_usuario'),
    path('<int:id>/actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('<int:id>/borrar/', views.borrar_usuario, name='borrar_usuario'),
]