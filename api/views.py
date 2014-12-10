from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.models import Profile,Hopital,HopitalTimeWait
from django.core import serializers
import json 

def toJson(data):
    return serializers.serialize('json',data)

def apiHopital(request):
    request.body = data
    data = json.loads(data)
    error = 'bad Json: '
    try:
        if request.method == 'GET':
            answer = toJson(Hopital.objects.all())
            return HttpResponse(answer)
        if request.method == 'POST':
            query = data['query']
            name = data['name']
            if query == 'select':
                try:
                    h = Hopital.objects.filter(name = name)[0]
                    return HttpResponse(toJson(h))
                except: 
                    error = 'Hospital ' + name + ' dose not exist.'
            if query = 'getWait':
                try:
                    h = Hopital.objects.filter(name = name)[0]
                    tmList = HopitalTimeWait.objects.filter(hopital = h)
                    lenTm = len(list(tmList))
                    tempsMoyen = 0

                    for i in tm: 
                        tempsMoyen += tm.waitTime

                    tempsMoyen = tempsMoyen / lenTm
                    answer = {'TempsMoyen':tempsMoyen,'Count':lenTm}
                    return HttpResponse(json.dumps(answer))
                except: 
                    error = 'Hospital ' + name + ' dose not exist.'


        if request.method == 'PUT':
            try:
                name = data['name']
                lat = data['lat']
                lng = data['lng']
                addr = data['addr']
                h = Hospital(name=name,lat=lat,lng=lng,addr = addr)
                h.save()
                HttpResponse('created/updated ' + name)
            except:
                error = 'missing informations'
        if request.method == 'DELETE':
            name = data['name']
            try:
                h = Hopital.objects.filter(name = name)[0].delete()
            except: 
                error = 'Hospital ' + name + ' dose not exist.'
            return HttpResponse('deleted ' + name)
    except: 
        return HttpResponse('Bad Json')

# Create your views here.
def apiProfile(request):
    request.body = data
    data = json.loads(data)
    error = 'bad Json: '
    try:
        if request.method == 'GET':
            answer = toJson(Profile.objects.all())
            return HttpResponse(answer)
        if request.method == 'POST':
            query = data['query']
            email = data['email']
            
            try:
                p = Profile.objects.filter(email = email)[0]
                if query == 'setHopital':
                    h = Hopital.objects.filter(name = name)[0]
                    p.hopital = h
                    p.save()

                if query == 'select':
                    return HttpResponse(toJson(p))
            except: 
                error = 'Profile ' + email + ' dose not exist.'

        if request.method == 'PUT':
            try:
                email = data['email']
                surname = data['surname']
                name = data['name']
                passowrd = data['password']
                age = data['age']
                googleKey = data['key']
                addr = data['addr']

                p = Profile(email=email,surname=surname,name=name,passowrd=passowrd,age=age,addr=addr,googleKey = googleKey)
                p.save()
                HttpResponse('created/updated ' + email)
            except:
                error = 'missing informations'
        if request.method == 'DELETE':
            email = data['email']
            try:
                p = Profile.objects.filter(email=email)[0].delete()
            except: 
                error = 'Profile ' + email + ' dose not exist.'
            return HttpResponse('deleted ' + email)
    except: 
        return HttpResponse('Bad Json')

def apiHopitalTimeWait(request):
    request.body = data
    data = json.loads(data)
    error = 'bad Json: '
    try:
        if request.method == 'GET':
            answer = toJson(HopitalTimeWait.objects.all())
            return HttpResponse(answer)
        if request.method == 'POST':
            query = data['query']

            try:
                if query == 'getHopitalWait':
                    hopitalName = data['hopitalName']
                    h = Hopital.objects.filter(hopitalName = hopitalName)[0]
                    waitList = HopitalTimeWait.objects.filter(hopital = h)
                    return HttpResponse(toJson(waitList))
                if query == 'updateWait':
                    email = data['email']
                    hopitalName = data['hopitalName']
                    h = Hopital.objects.filter(hopitalName = hopitalName)[0]
                    p = Profile.objects.filter(email = email)[0]
                    #rage = data['rage']
                    time = data['time']
                    hw = Hospital.objects.filter(profile=p,hospital=h)[0]
                    #hw.rageQuit = rage
                    hw.waitTime = wait
                    hw.save()
                    return HttpResponse('updated')

            except: 
                error = 'hopital ' + hopitalName + ' dose not exist.'

        if request.method == 'PUT':
            try:
                email = data['email']
                hopitalName = data['hopitalName']
                date = data['date']
                h = Hopital.objects.filter(hopitalName = hopitalName)[0]
                p = Profile.objects.filter(email = email)[0]
                hw HopitalTimeWait(profile=p,hospital=h,date=date,rageQuit='False',waitTime='0')
                hw.save()
                HttpResponse('created')
            except:
                error = 'missing informations'
        if request.method == 'DELETE':
            try:
                email = data['email']
                hopitalName = data['hopitalName']
                h = Hopital.objects.filter(hopitalName = hopitalName)[0]
                p = Profile.objects.filter(email = email)[0]
            
                hw = HopitalTimeWait.objects.filter(profile=p,hopital=h)[0].delete()
            except: 
                error = 'dose not exist.'
            return HttpResponse('deleted')
    except: 
        return HttpResponse('Bad Json')