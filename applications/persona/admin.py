from django.contrib import admin
from .models import Empleado , Habilidades
# Register your models here.

admin.site.register(Habilidades)

#esto es para decorar el admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #
    def full_name(self,obj): #busca todos los objetos que existen
        #toda la operacion que necesite 
        return obj.first_name +  ' ' + obj.last_name 
    
    #
    
    #filter and search
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades', 'departamento',)
    #
    filter_horizontal = ('habilidades',)
 

admin.site.register(Empleado , EmpleadoAdmin)