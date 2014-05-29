from django.shortcuts import render,render_to_response
from django.template import RequestContext
#from django.views.generic import TemplateView,FormView
from miproyecto.apps.logeo.forms import LoginForm,RegisterForm,ContactForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User






# Create your views he
def contacto_view(request):
	info_enviado=False#si se envio o no  la informacion
	email=""
	titulo=""
	texto=""
	if request.method=="POST":
		formulario=ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado=True
			nombre=formulario.cleaned_data['Nombre']
			email=formulario.cleaned_data['Email']
			titulo=formulario.cleaned_data['Titulo']
			texto=formulario.cleaned_data['Texto']
			#configuracion enviado mensaje via email
			
	else:
		formulario=ContactForm()
	ctx={'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('logeo/contacto.html',ctx,context_instance=RequestContext(request))



def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def login_view(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method=="POST":
			form=LoginForm(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/auth')
				else:
					mensaje="usuario y/o password incorrecto"
		form=LoginForm()
		ctx={'form':form,'mensaje':mensaje}
		return render_to_response('logeo/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/index/')

def register_view(request):
	form= RegisterForm()
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			usuario=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password_one=form.cleaned_data['password_one']
			password_two=form.cleaned_data['password_two']
			u=User.objects.create_user(username=usuario, email=email,password=password_one)
			u.save()#guardar el objecto
			return render_to_response('logeo/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx={'form':form}
			return render_to_response('logeo/register.html',ctx,context_instance=RequestContext(request))
	ctx={'form':form}

	return render_to_response('logeo/register.html',ctx,context_instance=RequestContext(request))




