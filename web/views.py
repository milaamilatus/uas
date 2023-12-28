from django.shortcuts import render
from django.http import HttpResponse

def beranda(request):
    return render(request, 'myweb/beranda.html')

def weblog(request):
    return render(request, 'myweb/weblog.html')

