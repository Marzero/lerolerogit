from django.shortcuts import render,render_to_response
from django.template import RequestContext
from  .forms import *
from .models import *


from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.

def registrarcliente(request):
	if request.method=="POST":
		form=registroCliente(request.POST)
		
		if(form.is_valid()):
		
			form.save();
			return render_to_response("cliente/clienteregistrado.html",{},RequestContext(request))
	form=registroCliente()
	return render_to_response("cliente/registrarcliente.html",{"form":form},RequestContext(request))

def registrodeclienteexito(request):
	form=cliente.objects.all()
	return render_to_response("cliente/clienteregistrado.html",{"form":form},RequestContext(request))