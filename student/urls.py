from django.urls import path
from .views import register_student

urlpatterns = [
    path('student/', register_student, name='student')

]