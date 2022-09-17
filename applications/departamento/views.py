from django.shortcuts import render
from django.views.generic import  ListView
from django.views.generic.edit import FormView
from applications import departamento
from applications.departamento.forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

#clases


class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/lista.html'
    context_object_name = 'departamentos'





class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):#recupera los datos
        print('********FORM VALID*******')
        #forma 1 de guardar formularios con relacion a modelos en base de datos
        depa = Departamento (
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name']
        )
        depa.save()
        #forma 2 "" ""
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        #aca se registran nomas lo obligatorio para la creacion en la base de datos
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job='1',
            departamento= depa,
        )
        

        return super(NewDepartamentoView, self).form_valid(form)
