from django.conf.urls import patterns, include, url
import contacts.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', analise.views.ListTweetView.as_view(),
                           name='tweet-list',),
                       
                       # Examples:
                       # url(r'^$', 'vtbr.views.home', name='home'),
                       # url(r'^vtbr/', include('vtbr.foo.urls')),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                   )
