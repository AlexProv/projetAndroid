from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.models import Profile,Hopital,HopitalTimeWait
from django.core import serializers
import json 

def toJson(data):
    return serializers.serialize('json',data)

def apiHopital(request):
    error = 'bad Json: '
    try:
        #GET############
        if request.method == 'GET':
            answer = toJson(Hopital.objects.all())
            return HttpResponse(answer)

        #POST############
        data = request.body
        data = json.loads(data)
        if request.method == 'POST':
            query = data['query']
            name = data['name']
            if query == 'select':
                try:
                    h = Hopital.objects.filter(name = name)
                    return HttpResponse(toJson(h))
                except: 
                    error = 'Hospital ' + name + ' dose not exist.'

            elif query == 'getWait':
                error = 'Hospital ' + name + ' dose not exist.'
                
                h = Hopital.objects.filter(name = name)[0]
                tmList = HopitalTimeWait.objects.filter(hopital = h)

                lenTm = len(list(tmList))
                tempsMoyen = 0

                if lenTm == 0:
                    answer = {'TempsMoyen':'0','Count':'0'}
                    return HttpResponse(json.dumps(answer))

                for i in tmList:

                    print i.waitTime
                    tempsMoyen += int(i.waitTime)

                tempsMoyen = tempsMoyen / lenTm
                answer = {'TempsMoyen':tempsMoyen,'Count':lenTm}
                return HttpResponse(json.dumps(answer))
            
                   

        #PUT###############
        if request.method == 'PUT':
            try:
                name = data['name']
                lat = data['lat']
                lng = data['lng']
                addr = data['addr']
                key = data['key']
                h = Hopital(name=name,lat=lat,lng=lng,addr = addr,googleKey = key)
                h.save()
                return HttpResponse('created/updated ' + name)
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
        return HttpResponse(error)

# Create your views here.
def apiProfile(request):
    error = 'bad Json: '
    try:
        if request.method == 'GET':
            answer = toJson(Profile.objects.all())
            return HttpResponse(answer)

        data = request.body 
        data = json.loads(data)
        if request.method == 'POST':
            query = data['query']
            email = data['email']
            try:
                if query == 'select':
                    p = Profile.objects.filter(email=email)
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

                p = Profile(email=email,surname=surname,name=name,password=passowrd,age=age)
                p.save()
                return HttpResponse('created/updated ' + email)
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
    try:
        if request.method == 'GET':
            answer = toJson(HopitalTimeWait.objects.all())
            return HttpResponse(answer)

        data = request.body
        data = json.loads(data)
        error = 'bad Json: '

        if request.method == 'POST':
            hopitalName = data['hopitalName']
            error = 'hopital ' + hopitalName + ' dose not exist.'
            
            query = data['query']
            if query == 'getHopitalWait':
                h = Hopital.objects.filter(name = hopitalName)[0]
                waitList = HopitalTimeWait.objects.filter(hopital = h)
                return HttpResponse(toJson(waitList))

            if query == 'updateWait':
                email = data['email']
                h = Hopital.objects.filter(name = hopitalName)[0]
                p = Profile.objects.filter(email = email)[0]

                time = data['time']
                hw = HopitalTimeWait.objects.filter(profile=p,hopital=h)[0]
                hw.waitTime = time
                hw.save()
                return HttpResponse('updated')
        
            

        if request.method == 'PUT':
            error = 'missing informations'

            email = data['email']
            hopitalName = data['hopitalName']
            date = data['date']

            h = Hopital.objects.filter(name = hopitalName)[0]
            p = Profile.objects.filter(email = email)[0]
            
            hw = HopitalTimeWait(profile=p,hopital=h,date=date,rageQuit='False',waitTime='0')
            
            hw.save()
            return HttpResponse('created')

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