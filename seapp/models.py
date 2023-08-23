from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.CharField(max_length=20,)
    cuit = models.CharField(max_length=20,)
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    email = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=202)
    fecha_nacimiento = models.DateField()
    SEXO =  [(1, "Masculino"),
            (2, "Femenino"),
            (3, "Otro"),]
    sexo = models.PositiveSmallIntegerField(choices = SEXO)
    localidad = models.CharField(max_length=120)
    provincia = models.CharField(max_length=120)
    pais = models.CharField(max_length=120, verbose_name="país")
    image = models.ImageField(upload_to="imgPerfil", null=True, blank=True, verbose_name="perfil")
    idiomas = models.CharField(max_length=50, null=True, blank=True)
    idiomas1 = models.CharField(max_length=50, null=True, blank=True)
    idiomas2 = models.CharField(max_length=50, null=True, blank=True)
    idiomas3 = models.CharField(max_length=50, null=True, blank=True)
    nivel_idioma = [(1, "Básico"),
                    (2, "Intermedio"),
                    (3, "Competente"),]
    niv_idioma = models.PositiveSmallIntegerField(choices= nivel_idioma)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    search_filter = ('nombre','apellido','dni','cuit','estudios_realizados')


    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ["-id"]

    def __str__(self):
        return self.nombre
    
class EstudioRealizado(models.Model):
    carrera = models.CharField(max_length=150)
    nivel_academico = [ (1, "Primario"),
                        (2, "Secundario"),
                        (3, "Terciario"),
                        (4, "Universitario"), ]
    niv_academico = models.PositiveSmallIntegerField (choices= nivel_academico, verbose_name="Nivel Academico")
    estado_estudios = [ (1, "Completo"),
                        (2, "Incompleto"),
                        (3, "En curso"), ]
    esta_estudios = models.PositiveSmallIntegerField (choices= estado_estudios, verbose_name="Estado de Estudios")
    #persona_estu_realizado= models.ForeignKey(Persona, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "estudio realizado"
        verbose_name_plural = "estudios realizados"
        ordering = ["-id"]

    def __str__(self):
        return self.carrera

class ExperienciaLaboral(models.Model):
    empresa = models.CharField (max_length=150)
    sector_empresa =  [ (1, "Recursos Humanos"),
                        (2, "Producción"),
                        (3, "Finanzas / Contabilidad"),
                        (4, "Marketing y Ventas"),
                        (5, "Tecnología"),
                        (6, "Servicio al Cliente"),
                        (7, "Sistemas"),
                        (8, "Calidad"), 
                        (9, "Logistica"),
                        (10, "Ingenieria"),
                        (11, "Dirección Ejecutiva"),
                        (12, "Otros"), ]
    sec_empresa = models.PositiveSmallIntegerField(choices= sector_empresa, verbose_name="Sector")
    persona_exp_laboral = models.ForeignKey (Persona, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "experiencia laboral"
        verbose_name_plural = "experiencias laborales"
        ordering = ["-id"]

    def __str__(self):
        return self.empresa 

class InformacionAdicional(models.Model):
    curso = models.CharField(max_length=150, verbose_name="Capacitación Tomada")
    instituto_cursado = models.CharField( max_length=120,)
    persona_info_adicional = models.ForeignKey (Persona, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "información adicional"
        verbose_name_plural = "informaciones adicionales"
        ordering = ["-id"]

    def __str__(self):
        return self.curso
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="Nombre Completo")
    email = models.EmailField()
    asunto = models.CharField(max_length=60, verbose_name="Asunto de su consulta")
    mensaje = models.TextField("Mensaje", blank=False , null= False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
