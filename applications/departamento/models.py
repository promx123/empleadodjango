from enum import unique
from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('nombre', max_length=50) #nombre es para que el admin lo vea mas amigable y si queremos que no se pueda editar este campo tenemos que agregar editable =false
    short_name = models.CharField('nombre corto', max_length=20, unique=True)
    anulate  = models.BooleanField('anulado', default=False )
    
    class Meta:
        verbose_name = 'Mi departamento'  #como queremos que se vea en el admin el nombre
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name'] #para ordenar  -name -> asi seria inverso 
        unique_together = ('name', 'short_name') # para que no se repita esa conbinacion 
     
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name