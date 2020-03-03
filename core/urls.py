# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("authentication.urls")),
    path("", include("app.urls")),
    path('admin/', admin.site.urls),


]
