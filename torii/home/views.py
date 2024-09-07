from django.shortcuts import render
from torii.institute.models import Subject, Gallery


def home(request):
    subjects = Subject.objects.filter(available=True)
    photos = Gallery.objects.all()
    return render(request, 'home/index.html', {'subjects': subjects, 'photos': photos})


def about(request):
    return render(request, 'home/about.html')
