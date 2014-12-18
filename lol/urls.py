from django.conf.urls import patterns, url
from lol.views import lol,apiHopital,apiProfile,apiHopitalTimeWait


urlpatterns = patterns('',
    url(r'^$', lol, name='lol'),
    url(r'^hopital/$', apiHopital, name='apiHopital'),
    url(r'^profile/$', apiProfile, name='apiProfile'),
    url(r'^wait/$', apiHopitalTimeWait, name='apiHopitalTimeWait'),
    
)