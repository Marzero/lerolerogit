from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from miproyecto.apps.almacen.forms import addProductForm
#from miproyecto.apps.almacen.models import producto
from .models import *
from .forms import *
import datetime
# Create your views here.

def add_product_view(request):
	if request.method=="POST":
		form=addProductForm(request.POST)
		info="Inicializando"
		if form.is_valid():
			form.save()
			"""nombre=form.cleaned_data['nombre']
			cantidad=form.cleaned_data['cantidad']
			precio=form.cleaned_data['precio']
			#cat=form.cleaned_data['cat']
			descripcion=form.cleaned_data['descripcion']
			p=producto()
			p.nombre=nombre
			p.cantidad=cantidad
			p.precio=precio
			#p.cat=cat
			p.descripcion=descripcion
			p.status=True
			p.save()"""
			info="Se guardo saticfactoriamente"
		else:#Get
			info="informacion e datos incorrectos"
		form=addProductForm()
		ctx={'form':form,'informacion':info}
		return render_to_response('almacen/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		form=addProductForm()
		ctx={'form':form}
		return render_to_response('almacen/addProducto.html',ctx,context_instance=RequestContext(request))
def add_categoria_view(request):
	if request.method=="POST":
		info="inicializando"
		form=addCategoria(request.POST)
		if form.is_valid():
			fecha=form.cleaned_data['fecha']
			nombreCategoria=form.cleaned_data['nombreCategoria']
			c=Categoria()
			c.nombreCategoria=nombreCategoria
			c.fecha=fecha
			c.save()
			info="se guardo exitosamente"
		else:
			info="datos incorrectos"
		form=addCategoria()
		ctx={'form':form,'informacion':info}
		return render_to_response("almacen/addCategoria.html",ctx,context_instance=RequestContext(request))
	else:
		form=addCategoria()
		ctx={'form':form}
		return render_to_response("almacen/addCategoria.html",ctx,context_instance=RequestContext(request))
def detalleProducto_view(request,id_prod):
	prod=producto.objects.get(id=id_prod)
	ctx={'producto':prod}
	return render_to_response("almacen/detalleProducto.html",ctx,context_instance=RequestContext(request))
#def productos_view(request):
#	prod=producto.objects.filter(status=True)
#	ctx={'producto':prod}
#	return render_to_response('almacen/producto.html',ctx,context_instance=RequestContext(request))
def listadodeTodo(request):
	lista=producto.objects.all()
	categorialista=Categoria.objects.all()
	return render_to_response("almacen/listados.html",{"lista":lista,"cate":categorialista},RequestContext(request))	
def ListadoPorCategoria(request,categoria):
	lista=list(producto.objects.filter(cat__id=categoria))
	categorialista=Categoria.objects.all()
	return render_to_response("almacen/listados.html",{"lista":lista,"cate":categorialista},RequestContext(request))
def borrarRel(request,idp,idc):
	pro=producto.objects.get(id=idp)
	cat=Categoria.objects.get(id=idc)
	pro.cat.remove(cat)
	pro.save()