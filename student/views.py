from django.shortcuts import render
from .forms import StudentRegistration


def register_student(request):
    msg = None
    success = False
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Student created.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = StudentRegistration()

    return render(request, "students/register.html", {"form": form, "msg": msg, "success": success})
