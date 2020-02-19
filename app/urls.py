# -*- encoding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, re_path, include
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
    path('', include('student.urls')),

]
