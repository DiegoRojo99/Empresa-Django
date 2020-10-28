from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
