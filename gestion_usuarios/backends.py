from django.contrib.auth.backends import BaseBackend
from .models import Usuarios
from django.contrib.auth.hashers import check_password

class UsuariosBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(usuario=username)
            # Comparar la contraseña ingresada con la almacenada (texto plano)
            if user.contraseña == password:
                return user
        except Usuarios.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Usuarios.objects.get(pk=user_id)
            # Añadimos un atributo is_active dinámico
            user.is_active = True
            return user
        except Usuarios.DoesNotExist:
            return None
