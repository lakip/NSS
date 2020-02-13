# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import Register
from .models import StudentRegister, Post


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


def SRegister(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            admno = request.POST.get('admno')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            town = form.cleaned_data.get('town', '')
            county = form.cleaned_data.get('county', '')
            postalcode = form.cleaned_data.get('postalcode')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            phone = form.cleaned_data.get('phone')

            register_obj = StudentRegister(admno=admno, first_name=first_name, last_name=last_name, address=address,
                                           town=town, county=county, postalcode=postalcode, fname=fname, lname=lname,
                                           phone=phone)
            register_obj.save()
            return HttpResponse('saved successfully', {'form': form})
        else:
            msg = 'Error validating the form'

    return render(request, 'pages/teacher_list.html')


def createpost(request):
    if request.POST.get('title') and request.POST.get('content'):
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return render(request, 'pages/create.html')

    else:
        return render(request, 'pages/create.html')


