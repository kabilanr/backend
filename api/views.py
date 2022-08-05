from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serialiezer import PersonSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def person_list(request):
    if request.method=='GET':
        t=Person.objects.all()
        detail=PersonSerializer(t,many=True)
        return JsonResponse(detail.data,safe=False)
    elif request.method=='POST':
       
        add=JSONParser().parse(request)
        print(add)
        ser=PersonSerializer(data=add)
        if ser.is_valid():
            ser.save()
        else:
            return JsonResponse(ser.errors,safe=False)
        
    return JsonResponse({"message":"Person added successfully"})

