from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # usado em dev

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import votos.views

urlpatterns = patterns('',
    url(r'^$', votos.views.ListVotosView.as_view(),
        name='votos',),
    url(r'^users/', votos.views.ListUsersView.as_view(),
        name='users',),
    url(r'^new$', votos.views.CreateUserView.as_view(),
        name='users-new',),
    url(r'^edit/(?P<pk>\d+)/$', votos.views.UpdateUserView.as_view(),
        name='users-edit',),
    url(r'^delete/(?P<pk>\d+)/$', votos.views.DeleteUserView.as_view(),
        name='users-delete',),
    url(r'^(?P<pk>\d+)/$', votos.views.UserView.as_view(),
        name='users-view',),
    url(r'^edit/(?P<pk>\d+)/votos$', votos.views.EditUserVotoView.as_view(),
        name = 'users-edit-votos',),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),                   
    # Examples:
    # url(r'^$', 'votobrasil.views.home', name='home'),
    # url(r'^votobrasil/', include('votobrasil.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns() # usado em dev
