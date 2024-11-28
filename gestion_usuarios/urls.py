from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
    path('jefe/', views.vista_jefe, name='vista_jefe'),
    path('despachador/', views.vista_despachador, name='vista_despachador'),
]
