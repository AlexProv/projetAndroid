from django.conf.urls import patterns, url
from api.views import apiHopital,apiHopitalTimeWait,apiProfile

urlpatterns = patterns('',
    url(r'^hopital/$', apiHopital, name='apiHopital'),
    url(r'^profile/$', apiProfile, name='apiProfile'),
    url(r'^wait/$', apiHopitalTimeWait, name='apiHopitalTimeWait'),
)