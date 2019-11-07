from django.contrib import admin
from .models import User, Dept, Class, Student, Course, Teacher, StudentCourse, Question, Answer
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class DeptAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')
    ordering = ['name']


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'sem', 'year', 'teacher')
    search_fields = ('id', 'course__name', 'sem', 'year')
    ordering = ['course__name', 'sem', 'year']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept')
    search_fields = ('id', 'name', 'dept__name')
    ordering = ['dept__name', 'id', 'name']


class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_class')
    search_fields = ('student__user', 'course_class__id', 'student__id', 'student__dept__name', 'student__dept__id')
    ordering = ('student__id', 'student__user', 'course_class__id')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'dept', 'batch')
    search_fields = ('user', 'id', 'dept__name', 'batch')
    ordering = ['id','user', 'dept__name', 'batch']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'dept', 'id')
    search_fields = ('user', 'dept__name', 'id')
    ordering = ['user', 'dept__name', 'id']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'q_class', 'date')
    search_fields = ('id', 'q_class', 'user__username', 'date')
    ordering = ['id', 'q_class', 'user__username', 'date']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ques', 'date')
    search_fields = ('id', 'ques', 'user__username', 'date')
    ordering = ['id', 'ques', 'user__username', 'date']


admin.site.register(User, UserAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
