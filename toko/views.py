from django.shortcuts import render
from django.http import HttpResponse

def buah(request):
    return render(request, 'myweb/buah.html')

def beli(request):
    return render(request, 'myweb/beli.html')

def total(request):
    return render(request, 'myweb/total.html')



