
from django.db import models
from django_resized import ResizedImageField



from ckeditor.fields import RichTextField

#importacion de un campo de un modelo para hacer foreing key
from applications.departamento.models import Departamento
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    
    
    
class Empleado(models.Model):
    #modelo para tabla empleado
    #con el job choices es un arraid para pasar distintos tipos de funciones a un campo
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name= models.CharField('Nombres', max_length=50) #mc para hacer este campo
    last_name= models.CharField('Apellidos', max_length=50)
    full_name = models.CharField(
                                'Nombres completos',
                                 max_length=120,
                                 blank=True
                                 )
    job = models.CharField('trabajos', max_length=1 , choices= JOB_CHOICES )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)#fk para hacer este campo y con esto hacer el foreing key importando departamento 
    avatar = ResizedImageField(size=[500, 400], upload_to='empleado', blank=True, null = True)
    #mimg es para las imagenes
    habilidades = models.ManyToManyField(Habilidades) #m2m para hacer este campo
    hoja_vida =  RichTextField()
    
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name