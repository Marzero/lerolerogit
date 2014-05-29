from django.forms import ModelForm
from django import forms
from .models import *
class registroCliente(forms.ModelForm):
	class Meta:
		model=cliente
	def clean(self):
		cleaned_data = super(registroCliente, self).clean()
		apellidos = cleaned_data.get('Apellidos')
		nombres = cleaned_data.get('Nombres')
		ci = cleaned_data.get('Nombres')
		direccion = cleaned_data.get('Nombres')
		email = cleaned_data.get('Nombres')
		usuario = cleaned_data.get('Nombres')
		password1 = cleaned_data.get('Nombres')
		password2 = cleaned_data.get('Nombres')
		lista=cliente.objects.filter(apellidos=apellidos,nombres=nombres,ci=ci,direccion=direccion,email=email,usuario=usuario,password1=password1,password2=password2)
		if(len(lista)>0):
			raise forms.ValidationError("El cliente Ya existe en la base de datos")
		return cleaned_data