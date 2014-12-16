from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile,Hopital,HopitalTimeWait
from django.core import serializers

# Create your views here.

def toJson(data):
    return serializers.serialize('json',data)


def lol(request):
    if request.method == 'PUT':
        print 'allo'
        data = toJson(Hopital.objects.all())
        print data
        print 'ya un prob'
        return HttpResponse(data)
    elif request.method == 'GET':
        return HttpResponse('notlol')
    elif request.method == 'POST':
        return HttpResponse()