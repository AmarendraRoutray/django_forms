from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def create_topic(request):
    
    if request.method == 'POST':
        tn=request.POST['tn']
        
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse(tn)
    
    return render(request,'create_topic.html')




def create_webpage(request):
    if request.method=='POST':
        tn = request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        
        n=request.POST['name']
        u=request.POST['url']
        e=request.POST['email']
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        
        return HttpResponse(n)
    
    return render(request,'create_webpage.html')