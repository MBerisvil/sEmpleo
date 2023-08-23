from django import forms    
from .models import Persona, EstudioRealizado, Contacto, InformacionAdicional, ExperienciaLaboral
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Persona_Form(forms.ModelForm):

    class Meta:
        model= Persona
        fields = '__all__'

class EstudioRealizado_Form(forms.ModelForm):

    class Meta:
        model= EstudioRealizado
        fields = '__all__'
        #fields = ["carrera","niv_academico","esta_estudios","persona_estu_realizado"]



class Contacto_Form(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class CrearUsuario_Form(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "is_enterprise", "last_name", "password1", "password2",] 

class InformacionAdicional_Form(forms.ModelForm):

    class Meta:
        model = InformacionAdicional
        fields = '__all__'

class ExperienciaLaboral_Form(forms.ModelForm):

    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'