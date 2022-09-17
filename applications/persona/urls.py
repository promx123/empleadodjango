from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"


urlpatterns = [
    path('', views.InicioView.as_view() , name= 'inicio'),
    path('listar_todo_empleados/', views.ListAllEmpleados.as_view() , name='empleados_all'),
    path('listar_by_area/<short_name>/', views.ListByAreaEmpleado.as_view(),name='empleados_area' ),
    path('listar_empleados_admin/', views.ListaEmpleadosAdmin.as_view(),name='empleados_admin' ),
    path('listar-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'), # pk es para id
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view() , name= 'modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view() , name= 'eliminar_empleado'),
       
]
