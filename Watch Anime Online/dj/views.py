from django.shortcuts import render
from django.http import HttpResponse
from . models import anime
from math import ceil
# Create your views here.
def index(request):
    return HttpResponse("hello")
def animelink(request):
    anm=anime.objects.all()
    print(anm)
    n= len(anm)
    nslides=n//4 + ceil((n/4)-(n//4))
    params={'no_slides':nslides, 'range':range(nslides),'ani': anm}
    return render(request,'dj/index.html',params)
def search(request):
    return HttpResponse("searchiiiiiiiing")