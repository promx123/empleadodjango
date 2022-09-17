from pickle import FALSE
from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , TemplateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from .models import  Empleado

####CARGA LA PAGINA DE INICIO
class InicioView(TemplateView):
    template_name = 'inicio.html'


#se usa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4 #esto lo podes comentar para ver si anda la pagination
    ordering = 'first_name'
    context_object_name = 'lista'
    #filtro
    def get_queryset(self):
        print('asdsadsadsa')
        palabra_clave = self.request.GET.get("kword" , '') ## buscar el metodo GET le pide un  name como kword  y lo encierra en palabra clave
        lista = Empleado.objects.filter(
            full_name__icontains= palabra_clave
        )
        #print('lista resultado' , lista)
        return lista
    
    #esta es la parte para el admin de empleados
    
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10 #esto lo podes comentar para ver si anda la pagination
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
        
    
    
    
    
######
    
 #se usa   
class ListByAreaEmpleado(ListView):
    #lista empleados de un area areas
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs ['short_name'] #kwargs es para agarrar datos que se mandan a la url
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista  
    

    #listar empleados por trabajos pendiente
    

    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        #definimos abajo que los empleados tienen diferentes habilidades sabiendo que antes haciamos relacion de habilidades tenian distintos empleado pero definimos particularmente para la tarea que necesitamos
        empleado = Empleado.objects.get(id=8)#hacerlo desde navegador con el method GET
        return empleado.habilidades.all()
    
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'
    #se usa para aclarar cosas del modelo al template y no tiene nada que ver con pasar objects.atribute
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView , self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes' 
        return context
    



    
     
class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    #fields = ['first_name','last_name' , 'job']  esta es una forma 
    #si queres todos los camposo
    #fields = ('__all__') esto es para llamar todos
    form_class = EmpleadoForm
    #success_url = '.' #este punto recarga la misma pagina
    success_url = reverse_lazy('persona_app:empleados_admin') #usamos reverse lazy porque funciona mejor y llamamos el app name + el name de la url
    
    #esta es una manera de editar datos ya guardados en la base de datos
    def form_valid(self, form):
        empleado = form.save(commit=FALSE) #asignas el formulario guardado a la variable pero con el commit false haces una instancia de guardado pero no guardas hasta el final de form save 
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView , self).form_valid(form) #esto indica que estamo sobrescribiendo el formvalid 
        


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************METODO POST**********')
        print('===================')
        print(request.POST) #aca recuperas diccionario de valores que es clave y valor
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
        
    success_url = reverse_lazy('persona_app:empleados_admin')

    
    
    
