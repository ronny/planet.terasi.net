from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'aggregator.views.home', name='home'),
    url(r'^update/$', 'aggregator.views.update', name='update'),

    url(r'^admin/', include(admin.site.urls)),
)
