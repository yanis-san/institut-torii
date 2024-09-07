
from django.contrib import admin
from django.urls import path
from torii.institute.views import japanese_courses,chinese_courses, korean_courses, other_courses, workshops


app_name = 'institute'

urlpatterns = [
    path('japonais/', japanese_courses,name="japanese"),
    path('chinois/', chinese_courses,name="chinese"),
    path('coréen/', korean_courses,name="korean"),
    path('ateliers/', workshops,name="workshops"),
    path('autre/', other_courses,name="other"),

]
