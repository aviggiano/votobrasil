from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import votos.views

urlpatterns = patterns('',
    url(r'^$', votos.views.ListVotosView.as_view(),
        name='votos',),
    url(r'^users/', votos.views.ListUsersView.as_view(),
        name='users',),
    # Examples:
    # url(r'^$', 'votobrasil.views.home', name='home'),
    # url(r'^votobrasil/', include('votobrasil.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
