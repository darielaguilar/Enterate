from django.db import models
from datetime import datetime
# Create your models here.
class Persona(models.Model):
    #Modelo de usuarios que usaran la app.
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=30,default='',unique=True)
    ip = models.GenericIPAddressField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to='Personas%Y/%m/%d')
    fecha_de_creacion = models.DateField(default=datetime.now,)
    fecha_de_actualizacion = models.DateField(default=datetime.now)
    cantidad_de_solicitudes = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.__str__()
            
        

    class Meta:
        db_table = 'Persona' 
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']


class Estadística(models.Model):
    Fecha = models.DateField(default=datetime.now)
    Total_personas = models.IntegerField()
    Total_solicitudes = models.IntegerField()

    def __str__(self) -> str:
        return self.Fecha.__str__()

    class Meta:
        db_table = 'Estadística'
        verbose_name = 'Estadística'
        verbose_name_plural = 'estadísticas'
        ordering = ['id']
    