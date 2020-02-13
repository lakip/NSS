# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include
from app.views import SRegister


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("app.urls")),
    path('', SRegister, name='registration'),

]
