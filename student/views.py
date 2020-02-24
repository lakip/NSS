from django.shortcuts import render
from .forms import StudentForm
from django.contrib import messages
from .models import StudentRegister

mss = ''


def studentform_view(request):
    if request.method == "POST":

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'registration successful')
            return render(request, 'students/class_list.html')
        else:
            return render(request, 'students/register.html')

    form = StudentForm
    return render(request, "students/register.html", {"form": form})


def class_list(request):
    context = {
        'student_list': StudentRegister.objects.all()
    }
    return render(request, 'students/class_list.html', context)

