
from django.contrib import admin
from django.urls import path
from torii.home.views import home, about


app_name = 'home'

urlpatterns = [
    path('', home,name="homepage"),
    path('about/', about,name="about"),


]
