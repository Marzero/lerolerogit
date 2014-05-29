from django.conf.urls import patterns, include, url


urlpatterns = patterns('miproyecto.apps.logeo.views',
    # Examples:
    # url(r'^$', 'Hotel1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$','index_view',name='vista_principal'),
    #url(r'^about/$','about_view',name='vista_about'),
    url(r'^login/$','login_view',name='vista_login'),
    url(r'^logout/$','logout_view',name='vista_logout'),
    url(r'^registro/$','register_view', name='vista_registro' ),
    #url(r'^productos/$','productos_view', name='vista_productos' ),
    url(r'^contacto/$','contacto_view', name='vista_contacto' ),
   
	#url(r'^registrarse/$', Registrarse, name='registrarse'),
	
)

