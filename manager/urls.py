from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('course/<int:course_id>/', courses, name='courses_detail'),
    path('lesson/<int:lesson_id>/', lessons, name='lessons_detail')
]