from django.db import models
import math
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete

# Create your models here.
sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

test_name = (
    ('Quiz 1', 'Quiz 1'), 
    ('Quiz 2', 'Quiz 2'),
    ('Mid Sem', 'Mid Sem'),
    ('End Sem', 'End Sem')
)

days = {
	'Sunday' : 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
}

sem_type = (
	('Even', 'Even'),
	('Odd', 'Odd'),
)


class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False


class Dept(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    id = models.CharField(primary_key=True, max_length=100, default=1)
    batch = models.IntegerField(default=2019)
    DOB = models.DateField(default='1999-01-01')

    def __str__(self):
        d = User.objects.get(username=self.user)
        return '%s : %s' % (d.get_full_name(), self.id)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')

    def __str__(self):
        d = User.objects.get(username=self.user)
        return '%s : %s' % (d.get_full_name(), self.id)


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, db_index=False)
    sem = models.CharField(max_length=50, choices=sem_type, default='Odd')
    year = models.IntegerField(default=2019)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, db_index=False)

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Course.objects.get(name=self.course)
        return '%s : %s %d' % (d.name, self.sem, self.year)

    @property
    def is_student_class(self) :
        x = StudentCourse.objects.filter(course_class=self)
        y = []
        for items in x :
            y.append(items.student)
        return y

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = (('student', 'course_class'))

    def __str__(self):
        return '%s : %s' % (self.student, self.course_class)


class Question(models.Model) :
	id = models.AutoField(primary_key=True)
	q_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
	content = models.CharField(max_length=1000)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	date = models.DateTimeField()
	answered = models.IntegerField(default=0)

	def __str__(self):
		return '%s' % (self.id)


class Answer(models.Model):
	id = models.AutoField(primary_key=True)
	ques = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	date = models.DateTimeField(auto_now=True)
	content = models.CharField(max_length=10000)

	def __str__(self):
		return '%s' % (self.id)


# Triggers


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

