from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.studentform_view, name='student'),
    path('edit<int:pk>/', views.student_update, name='update_student'),
    path('delete<int:pk>/', views.delete_student, name='delete_student'),
    path('classlist/', views.class_list, name='classlist'),
    # path('search/', views.searchposts, name='search')

]
