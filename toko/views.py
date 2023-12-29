from django.shortcuts import render
from django.http import HttpResponse

def buah(request):
    return render(request, 'myweb/buah.html')


