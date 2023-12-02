import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from.models import Facebook

# Create your views here.
def home(request):
    if request.method=="POST":
       puthu_link=request.POST.get('page','')
       urls=requests.get(puthu_link)
       bs=BeautifulSoup(urls.text,'html.parser')

       for link in bs.find_all('a'):
            new_link=link.get('href')
            new_name=link.string
            Facebook.objects.create(stringname=new_link,links=new_name)
       return HttpResponseRedirect('/')
    else:
       data_values=Facebook.objects.all()

    return render(request,'home.html',{'data_values':data_values})
