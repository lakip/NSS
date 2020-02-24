from django.urls import path
from .views import teacher_view, teacher_list

urlpatterns = [
    path('teacher/', teacher_view, name='teacher'),
    path('teacher_list/', teacher_list, name='list')
]