from django.urls import path
from.import views

urlpatterns = [
    path('', views.buah, name='buah.html'),
]