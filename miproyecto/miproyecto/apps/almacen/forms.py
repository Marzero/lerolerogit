from django import forms
from django.forms import ModelForm
from .models import *

class addProductForm(forms.ModelForm):
	#nombre=forms.CharField(widget=forms.TextInput())
	#descripcion=forms.CharField(widget=forms.TextInput())
	class Meta:
		model=producto
	#def clean(self):
	#	return self.cleaned_data
		#nombre=forms.CharField(widget=forms.TextInput())cla
class addCategoria(forms.ModelForm):
	class Meta:
		model=Categoria