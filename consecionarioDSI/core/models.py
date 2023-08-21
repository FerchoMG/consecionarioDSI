from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Project (models.Model):
    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=200, verbose_name= "Titulo")
    price = models.CharField(max_length=15, verbose_name= "Precio")
    image= models.ImageField(verbose_name= "Imagen", upload_to="cars")
    description = models.CharField(max_length=500, verbose_name= "Descripcion")
    motor = models.CharField(max_length=100, verbose_name= "Motor")
    cilindraje = models.CharField(max_length=100, verbose_name= "Cilindraje")
    horsepower = models.CharField(max_length=100, verbose_name= "Caballos De Fuerza")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Actualizado")
    def __str__(self):
        return self.tittle   
      
class info (models.Model):
    id_info = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name= "name")
    email = models.CharField(max_length=200, verbose_name= "email")
    message = models.CharField(max_length=15, verbose_name= "Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Creado")

    def __str__(self):
        return self.name   
       
class Meta:
    verbose_name= 'carro'
    verbose_name_plural = 'carros'
    ordering= ["-created"]

    def __str__(self):
        return self.title
    

 