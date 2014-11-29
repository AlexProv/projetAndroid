from django.conf.urls import patterns, url
from api.views import api

urlpatterns = patterns('',
    url(r'^$', api, name='api'),
)