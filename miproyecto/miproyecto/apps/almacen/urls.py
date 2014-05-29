from django.conf.urls import patterns, url
from .views import listadodeTodo,ListadoPorCategoria,borrarRel


urlpatterns = patterns('miproyecto.apps.almacen.views',

	#url(r'^registrarse/$', Registrarse, name='registrarse'),
	url(r'^add/producto/$','add_product_view',name="vista_agregar_producto"),
	url(r'^add/Categoria/$','add_categoria_view',name="vista_agregar_categoria"),
	url(r'^add/productos/(?P<id_prod>.+)/$','detalleProducto_view',name="vista_detalle_producto"),
		#url(r'^producto/$','productos_views',name="vista_productos"),
	url(r'^all/$','listadodeTodo',name="vista_todo"),
	url(r'^all/(?P<categoria>\d+)/$',ListadoPorCategoria),
   	url(r'^all/(?P<idp>\d+)/(?P<idc>\d+)/$',borrarRel)
)

