from django.shortcuts import render
from torii.institute.models import Subject, Course


def japanese_courses(request):
    subject_title = "Japonais"
    courses = Course.objects.filter(subject__title="Japonais")

    return render(request,'institute/japanese.html', context={"courses": courses, "subject_title": subject_title})




def chinese_courses(request):
    subject_title = "Chinois"
    courses = Course.objects.filter(subject__title="Chinois")

    return render(request, 'institute/chinese.html', context={"courses": courses, "subject_title": subject_title})


def korean_courses(request):
    subject_title = "Coréen"
    courses = Course.objects.filter(subject__title="Coréen")

    return render(request, 'institute/korean.html', context={"courses": courses, "subject_title": subject_title})




def other_courses(request):
    subject_title = "Autres"
    courses = Course.objects.filter(subject__title="Autres")

    return render(request, 'institute/other.html', context={"courses": courses, "subject_title": subject_title})



def workshops(request):
    subject_title = "Ateliers"
    courses = Course.objects.filter(subject__title="Ateliers")

    return render(request, 'institute/workshop.html', context={"courses": courses, "subject_title": subject_title})

