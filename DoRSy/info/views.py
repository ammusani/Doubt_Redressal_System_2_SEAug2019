from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Dept, Class, Student, Course, Teacher, Assign, DAYS_OF_WEEK, StudentCourse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/t_homepage.html')
    if request.user.is_student:
        return render(request, 'info/homepage.html')
<<<<<<< HEAD
    return render(request, 'info/logout.html')

def nopageerror(request):
	return render(request, 'info/error.html')
=======
    return render(request, 'info/logout.html')
>>>>>>> 2e32c2472bf41fcdddbabe04478545049f0e8299
