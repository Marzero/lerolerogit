from django.conf.urls import patterns, include, url
from miproyecto.apps.almacen.views import *
from miproyecto.apps.logeo.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HotelExito.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('miproyecto.apps.logeo.urls')),
    url(r'^index/', index_view),
    url(r'^almacen/', include('miproyecto.apps.almacen.urls')),
    url(r'^cliente/', include('miproyecto.apps.cliente.urls')),
    #url(r'^all1/',listadodeTodo)
   
    
)
