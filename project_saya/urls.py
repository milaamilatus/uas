from django.contrib import admin
from django.urls import path
from toko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda', beranda, name='beranda'),
    path('weblog/', weblog, name='weblog'),
    
]
