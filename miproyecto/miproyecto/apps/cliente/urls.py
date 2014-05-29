from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	
    url(r'^registrocliente/$',registrarcliente),
    url(r'^clienteregistrado/$',registrodeclienteexito),
    
)