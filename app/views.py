# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import Register
from .models import StudentRegister


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}

    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))
    except:

        template = loader.get_template('pages/error-404.html')
        return HttpResponse(template.render(context, request))


def student_register(request):
    if request.method == 'POST':
        Register.objects.create(text=request.POST['admno'])
        return redirect('/')

    return render(request, 'pages/register.html')