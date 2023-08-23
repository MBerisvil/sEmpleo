from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import Persona_Form, EstudioRealizado_Form, Contacto_Form, CrearUsuario_Form, InformacionAdicional_Form, \
    ExperienciaLaboral_Form
from .models import Persona, EstudioRealizado, InformacionAdicional
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import authenticate,login



# Create your views here.
def base(request):
    return render(request, "seapp/base.html")

#@login_required  # Decorador para que solo los usuarios logueados puedan acceder
def index(request):
    return render(request, "seapp/index.html")


@login_required
def persona(request):

    data = {
        "form" : Persona_Form()
    }

    if request.method == 'POST':
        formulario = Persona_Form(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos Cargados.")
            data["message"] = "Datos cargados"
        else:
            data["form"] = formulario

    return render(request, "seapp/persona.html",data)


def modificar_persona(request, id):

    persona = get_object_or_404(Persona, id=id)

    data = {
        'form' : Persona_Form(instance=persona)
    }

    if request.method == 'POST':
        formulario = Persona_Form(data=request.POST, instance=persona, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="persona.html")
        data["form"] = formulario

    return render(request, "seapp/modificarpersona.html", data)


# -- REVISAR FORMULARIO --***
@login_required
def estudiorealizado(request):
    data = {

        "form" : EstudioRealizado_Form()
    }
    

    if request.method == 'POST':
        formulario = EstudioRealizado_Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos Cargados.")
            data["message"] = "Datos Cargados"
        else:
            data["form"] = formulario

    return render(request, "seapp/estudiorealizado.html",data)


def contacto(request):
    data = {
        "form" : Contacto_Form()
    }

    if request.method == 'POST':
        formulario = Contacto_Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Consulta enviada.")
            data["message"] = "Consulta Enviada"
        else:
            data["form"] = formulario
    return render(request, "seapp/contacto.html", data)

#forma de enviar los datos por formulario


#Create views of list
@login_required
def listado_candidatos(request,):
    persona = Persona.objects.all()
    estudiorealizado = EstudioRealizado.objects.all()

    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(persona, 15)
        persona = paginator.page(page)
    except:
        raise Http404


    data ={
        'entity' : persona, #pongo que se llama entity para poder utilizar el paginador.
        'paginator' : paginator
        #'estudiorealizado' : estudiorealizado,
    }

    return render(request, "seapp/listadocandidatos.html", data)


#Update date of information.
#para realizar una modificacion debo solicitar el id del registro a modificar.


def registrarse(request):

    data = {
        'form' : CrearUsuario_Form()
    }

    if request.method == 'POST':
        formulario = CrearUsuario_Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al Home
            return redirect(to="index.html")
        data ["form"] = formulario

    return render(request, "registration/registrarse.html", data)

@login_required
def informacionadicional(request):
    
    data = {

        'form' : InformacionAdicional_Form()
    }

    if request.method == 'POST':
        formulario = InformacionAdicional_Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Información Adicional Registrada Correctamente!")
            data['message']="Información Adicional Registrada!"
        else:
            data["form"] = formulario

    return render(request, "seapp/informacionadicional.html", data)

@login_required
def experiencialaboral(request):
    data = {
        'form' : ExperienciaLaboral_Form(),
    }
    
    if request.method == 'POST':
        formulario = ExperienciaLaboral_Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Experiencia Laboral Registrada!")
            data ['message']= "Experiencia laboral registrada"
        else:
            data["form"] = formulario

    return render(request, "seapp/experiencialaboral.html", data)


def listado_uni(request):
    carreras = EstudioRealizado.objects.all().order_by('carrera')
    return render(request, 'listado_candidatos.html', {"carreras": carreras})


def is_admin(user):
    return user.groups.filter(name='Administrador').exists()