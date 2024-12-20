from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *


def index(request):
    courses = Course.objects.all()
    lessons = Lessons.objects.all()

    context = {
        'courses': courses,
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def courses(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lessons.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lessons,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def lessons(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)

    context = {
        'lesson': lesson,
        'current_year': datetime.now().year
    }

    return render(request, 'detail.html', context)
