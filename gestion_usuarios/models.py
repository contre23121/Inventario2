from django.db import models

class Usuarios(models.Model):
    usuarioid = models.AutoField(db_column='UsuarioID', primary_key=True)  # ID del usuario
    nombres = models.CharField(db_column='Nombres', max_length=100)
    apellidos = models.CharField(db_column='Apellidos', max_length=100)
    genero = models.CharField(db_column='Genero', max_length=10)
    email = models.CharField(db_column='Email', max_length=100)
    usuario = models.CharField(db_column='Usuario', max_length=50, unique=True)
    contraseña = models.CharField(db_column='Contraseña', max_length=255)
    rolid = models.IntegerField(db_column='RolID')
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(db_column='last_login', null=True, blank=True)

    class Meta:
        managed = False  # No permitir que Django intente crear la tabla
        db_table = 'Usuarios'  # Mapea con la tabla existente

    def __str__(self):
        return self.usuario

    @property
    def is_authenticated(self):
        # Esto se utiliza para saber si el usuario está autenticado o no
        return True
