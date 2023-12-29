from django.shortcuts import render
from django.http import HttpResponse

def fashion(request):
    return render(request, 'myweb/fashion.html')


