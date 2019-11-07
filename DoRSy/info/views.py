from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Dept, Class, Student, Course, Teacher, DAYS_OF_WEEK, StudentCourse, Question, Answer
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/t_homepage.html')
    if request.user.is_student:
        return render(request, 'info/homepage.html')
    return render(request, 'info/logout.html')

@login_required()
def viewcourse(request, stud_id):
    stud = Student.objects.get(id=stud_id)
    att_list = StudentCourse.objects.filter(student=stud)
    return render(request, 'info/courses.html', {'att_list': att_list})

@login_required()
def t_viewcourse(request, teach_id):
    teach = Teacher.objects.get(id=teach_id)
    ass_list = Class.objects.filter(teacher=teach)
    att_list = []
    y = set()
    for x in ass_list :
    	y.add(x.course.id)

    for i in y :
    	att_list.append(Course.objects.get(id=i))
    return render(request, 'info/t_courses.html', {'att_list': att_list})

@login_required()
def t_viewclass(request, teach_id):
    teach = Teacher.objects.get(id=teach_id)
    att_list = Class.objects.filter(teacher=teach)
    return render(request, 'info/t_classes.html', {'att_list': att_list})

@login_required()
def course_stream(request, c_class_id, stud_id):
	c_class = Class.objects.get(id=c_class_id)
	stud = Student.objects.get(id=stud_id)
	att_list1 = Question.objects.filter(q_class=c_class).order_by('-date')
	att_list2 = Class.objects.filter(course=c_class.course).order_by('-year')
	att_list3 = stud
	att_list4 = c_class
	return render(request, 'info/course_stream.html', {'att_list1' : att_list1, 'att_list2' : att_list2, 'att_list3' : att_list3, 'att_list4' : att_list4})

@login_required()
def t_course_stream(request, c_class_id, teach_id):
	c_class = Class.objects.get(id=c_class_id)
	teach = Teacher.objects.get(id=teach_id)
	att_list1 = Question.objects.filter(q_class=c_class).order_by('-date')
	att_list2 = Class.objects.filter(course=c_class.course).order_by('-year')
	att_list3 = teach
	att_list4 = c_class
	return render(request, 'info/t_course_stream.html', {'att_list1' : att_list1, 'att_list2' : att_list2, 'att_list3' : att_list3, 'att_list4' : att_list4})

@login_required()
def t_recent_course_stream(request, course_id, teach_id):
	c = Course.objects.get(id=course_id)
	att_list2 = Class.objects.filter(course=c).order_by('-year')
	c_class = att_list2[0]
	teach = Teacher.objects.get(id=teach_id)
	att_list1 = Question.objects.filter(q_class=c_class).order_by('-date')
	att_list3 = teach
	att_list4 = c_class
	return render(request, 'info/t_course_stream.html', {'att_list1' : att_list1, 'att_list2' : att_list2, 'att_list3' : att_list3, 'att_list4' : att_list4})

@login_required()
def viewques(request, q_id, u_id, p_id):
	q = Question.objects.get(id=q_id)
	ans = Answer.objects.filter(ques=q)
	return render(request, 'info/question.html', {'att_list1' : q, 'att_list2' : u_id, 'att_list3' : ans, 'id' : p_id})

@login_required()
def t_viewques(request, q_id, u_id, p_id):
	q = Question.objects.get(id=q_id)
	ans = Answer.objects.filter(ques=q)
	return render(request, 'info/t_question.html', {'att_list1' : q, 'att_list2' : u_id, 'att_list3' : ans, 'id' : p_id})

@login_required()
def postans(request, q_id, u_id, p_id):
	content = request.POST['a_text']
	ques = Question.objects.get(id=q_id)
	st = Student.objects.get(id=u_id)
	q_user = st.user
	ques.answered = ques.answered + 1
	ques.save()
	a = Answer.objects.create(ques=ques, content=content, user=q_user)
	a.save()
	return HttpResponseRedirect(reverse('viewques', args=(q_id, u_id, p_id)))

@login_required()
def t_postans(request, q_id, u_id, p_id):
	content = request.POST['a_text']
	ques = Question.objects.get(id=q_id)
	teach = Teacher.objects.get(id=u_id)
	q_user = teach.user
	ques.answered = ques.answered + 1
	ques.save()
	a = Answer.objects.create(ques=ques, content=content, user=q_user)
	a.save()
	return HttpResponseRedirect(reverse('t_viewques', args=(q_id, u_id, p_id)))

@login_required()
def forpost(request, ques_class_id, q_user_id):
	ques_class = Class.objects.get(id=ques_class_id)
	return render(request, 'info/postques.html', {'att_list1' : ques_class_id, 'att_list2' : q_user_id, 'att_list3' : ques_class})

@login_required()
def t_forpost(request, ques_class_id, q_user_id):
	ques_class = Class.objects.get(id=ques_class_id)
	return render(request, 'info/t_postques.html', {'att_list1' : ques_class_id, 'att_list2' : q_user_id, 'att_list3' : ques_class})

@login_required()
def postques(request, ques_class_id, q_user_id):
	content = request.POST['q_text']
	ques_class = Class.objects.get(id=ques_class_id)
	st = Student.objects.get(id=q_user_id)
	q_user = st.user
	q = Question.objects.create(q_class=ques_class, content=content, user=q_user, date=datetime.datetime.now())
	q.save()
	return HttpResponseRedirect(reverse('course_stream', args=(ques_class.id, q_user.student.id)))

@login_required()
def t_postques(request, ques_class_id, q_user_id):
	content = request.POST['q_text']
	ques_class = Class.objects.get(id=ques_class_id)
	teach = Teacher.objects.get(id=q_user_id)
	q_user = teach.user
	q = Question.objects.create(q_class=ques_class, content=content, user=q_user, date=datetime.datetime.now())
	q.save()
	return HttpResponseRedirect(reverse('t_course_stream', args=(ques_class.id, q_user.teacher.id)))

@login_required()
def personalques(request, u_id):
	st = Student.objects.get(id=u_id)
	q_user = st.user
	q = Question.objects.filter(user=q_user).order_by('-date')
	return render(request, 'info/personalques.html', {'att_list' : q})

@login_required()
def t_personalques(request, u_id):
	teach = Teacher.objects.get(id=u_id)
	q_user = teach.user
	q = Question.objects.filter(user=q_user).order_by('-date')
	return render(request, 'info/t_personalques.html', {'att_list' : q})

@login_required()
def personalans(request, u_id):
	st = Student.objects.get(id=u_id)
	a_user = st.user
	a = Answer.objects.filter(user=a_user).order_by('-date')
	return render(request, 'info/personalans.html', {'att_list' : a})

@login_required()
def t_personalans(request, u_id):
	teach = Teacher.objects.get(id=u_id)
	a_user = teach.user
	a = Answer.objects.filter(user=a_user).order_by('-date')
	return render(request, 'info/t_personalans.html', {'att_list' : a})

@login_required()
def viewpersonalans(request, a_id, u_id):
	a = Answer.objects.get(id=a_id)
	return render(request, 'info/viewpersonalans.html', {'att_list1' : a.ques, 'att_list2' : u_id, 'att_list3' : a})

@login_required()
def t_viewpersonalans(request, a_id, u_id):
	a = Answer.objects.get(id=a_id)
	return render(request, 'info/t_viewpersonalans.html', {'att_list1' : a.ques, 'att_list2' : u_id, 'att_list3' : a})

def nopageerror(request):
	return render(request, 'info/error.html')
