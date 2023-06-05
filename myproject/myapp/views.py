from django.shortcuts import render
from django.http import HttpResponse

# python manage.py runserver

# Create your views here.
def index(request):
   return render(request,'index.html')

def counter(request):
   text= request.GET['text']
   return render(request, 'counter.html')