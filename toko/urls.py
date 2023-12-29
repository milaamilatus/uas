from django.urls import path
from.import views

urlpatterns = [
    path('', views.fashion, name='fashion.html'),
]