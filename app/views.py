from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def create_topic(request):
    
    if request.method == 'POST':
        tn=request.POST['tn']
        
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        
        QLTO = Topic.objects.all()
        d = {'topics':QLTO}
        return render(request,'display_topic.html',d)
    
    return render(request,'create_topic.html')




def create_webpage(request):
    QLTO = Topic.objects.all()
    d = {'topics':QLTO}
    if request.method=='POST':
        tn = request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        
        n=request.POST['name']
        u=request.POST['url']
        e=request.POST['email']
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        
        QLWO = Webpage.objects.all()
        
        return render(request,'display_webpage.html',{'webpage':QLWO})
    
    return render(request,'create_webpage.html',d)


def select_multiple_webpages(request):
    QLTO = Topic.objects.all()
    d = {'topics':QLTO}
    
    if request.method=='POST':
        topicList=request.POST.getlist('tname') #[list of selected topics]
        # print(topicList)
        
        QLWO = Webpage.objects.none()   # creating empty queryset using none() method
        for topic in topicList:
            QLWO = QLWO | Webpage.objects.filter(topic_name=topic)  # concatenating every topic to empty queryset using parallel pipe
            
        d = {'webpage':QLWO}
        return render(request,'display_webpage.html',d)
    
    return render(request,'select_multiple_webpages.html',d)


# url navigation # action attribute in chechBox.html file
def chechBox(request):
    QLTO = Topic.objects.all()
    return render(request,'chechBox.html',{'topic':QLTO})









def create_accessrecords(request):
    QLWO = Webpage.objects.all()
    d={'name':QLWO}
    if request.method=='POST':
        n = request.POST['name']
        WO = Webpage.objects.get(name=n)
        
        au = request.POST['au']
        dt = request.POST['dt']
        
        AO = AccessRecords.objects.get_or_create(name=WO,author=au,date=dt)
        
        AQLO = AccessRecords.objects.all()
        d = {'accessrecords':AQLO}
        
        return render(request, 'display_accessrecords.html',d)
    return render(request,'create_accessrecords.html',d)



def select_multiple_accessrecords(request):
    QLWO=Webpage.objects.all()
    d = {'webpage':QLWO}
    if request.method=='POST':
        nameList = request.POST.getlist('name')
        
        QLAO = AccessRecords.objects.none()
        for nm in nameList:
            QLAO = QLAO | AccessRecords.objects.filter(name=nm)
        d = {'accessrecords':QLAO}
        return render(request,'display_accessrecords.html',d)
        
    
    return render(request,'select_multiple_accessrecords.html',d)