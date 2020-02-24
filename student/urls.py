from django.urls import path
from . import views

urlpatterns = [
    # path('student/', views.register_student, name='student'),
    path('student/', views.studentform_view, name='student'),
    path('classlist/', views.class_list, name='classlist')

]