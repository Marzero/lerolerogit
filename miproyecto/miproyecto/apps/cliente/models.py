from django.db import models

# Create your models here.
class cliente(models.Model):
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	ci = models.IntegerField(max_length=8)
	direccion = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	usuario = models.CharField(max_length=50)
	password1 = models.CharField(max_length=50)
	password2= models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombres