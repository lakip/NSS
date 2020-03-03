from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import StudentRegister

mss = ''


def studentform_view(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = StudentRegister.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, 'students/register.html', {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/class_list.html')
        else:
            return render(request, 'students/register.html')
    #
    form = StudentForm
    return render(request, "students/register.html", {"form": form})


def student_update(request, pk, template_name='students/update_student.html'):
    student = get_object_or_404(StudentRegister, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student/')
    return render(request, template_name, {'form':form})


def delete_student(request, pk, template_name='students/class_list.html'):
    student = get_object_or_404(StudentRegister, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.delete()
        return redirect('student/')
    return render(request, template_name, {'form':form})


def class_list(request):
    context = {
        'student_list': StudentRegister.objects.all()
    }
    return render(request, 'students/class_list.html', context)
