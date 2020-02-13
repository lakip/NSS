# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from .views import SRegister, Post

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),

    path('', views.index, name='home'),
    path('', SRegister, name='registration'),
    path('post/', Post)

]
