from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombreCategoria=models.CharField(max_length=200)
	fecha=models.DateField()
	def __unicode__(self):
		return "%s"%(self.nombreCategoria)
class producto(models.Model):
	"""def url(self,filename):
		ruta="static/MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta"""
	nombre=models.CharField(max_length=100)
	cantidad=models.DecimalField(max_digits=3,decimal_places=0)
	imagen=models.ImageField(upload_to='Media',null=True,blank=True)
	precio=models.DecimalField(max_digits=5,decimal_places=2)
	fecha=models.DateField(auto_now=True)
	cat=models.ManyToManyField(Categoria)
	descripcion=models.TextField(max_length=300)
	status=models.BooleanField(default=True)
	def __unicode__(self):
		return "%s"%(self.nombre)
