from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from aggregator.feed import LatestEntriesFeed, AtomLatestEntriesFeed

urlpatterns = patterns('',
    url(r'^$', 'aggregator.views.home', name='home'),
    url(r'^update/$', 'aggregator.views.update', name='update'),
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),
    url(r'^rss20.xml$', LatestEntriesFeed(), name='rss'),
    url(r'^atom.xml$', AtomLatestEntriesFeed(), name='atom'),
    url(r'^opml.xml$', 'aggregator.views.opml', name='opml'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

