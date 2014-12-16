from django.conf.urls import patterns, url
from lol.views import lol

urlpatterns = patterns('',
    url(r'^$', lol, name='lol'),
    
    
)