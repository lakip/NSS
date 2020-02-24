from django.shortcuts import render
from .forms import TeacherForm
from .models import TReacher


def teacher_view(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/teachers_list.html')
        else:
            return render(request, 'teachers/teachers_register.html')
    form = TeacherForm
    return render(request, 'teachers/teachers_register.html', {"form": form})


def teacher_list(request):
    context = {
        'teacher_list': TReacher.objects.all()
    }
    return render(request, 'teachers/teachers_list.html', context)


