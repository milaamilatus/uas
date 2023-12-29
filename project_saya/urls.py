from django.contrib import admin
from django.urls import path
from toko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buah',buah, name='buah'),
    path('beli',beli, name='beli')
]
