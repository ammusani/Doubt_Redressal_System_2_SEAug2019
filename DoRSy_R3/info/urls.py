from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<slug:stud_id>/viewcourse/', views.viewcourse, name='viewcourse'),
    path('teacher/<slug:teach_id>/t_viewclass/', views.t_viewclass, name='t_viewclass'),
    path('student/<str:c_class_id>/<str:stud_id>/coursestream/', views.course_stream, name='course_stream'),
    path('student/<str:c_class_id>/<str:stud_id>/post_disable_coursestream/', views.post_disable_course_stream, name='post_disable_course_stream'),
    path('student/<str:ques_class_id>/<str:q_user_id>/forpost/', views.forpost, name='forpost'),
    path('student/<str:ques_class_id>/<str:q_user_id>/postquestion/', views.postques, name='postques'),
    path('student/<str:q_id>/<str:u_id>/<str:p_id>/viewques/', views.viewques, name='viewques'),
    path('student/<str:q_id>/<str:u_id>/<str:p_id>/post_disable_viewques/', views.post_disable_viewques, name='post_disable_viewques'),
    path('student/<str:q_id>/<str:u_id>/<str:p_id>/postans/', views.postans, name='postans'),
    path('student/<str:u_id>/personalques/', views.personalques, name='personalques'),
    path('student/<str:u_id>/personalans/', views.personalans, name='personalans'),
    path('student/<str:a_id>/<str:u_id>/viewpersonalans/', views.viewpersonalans, name='viewpersonalans'),
    path('teacher/<str:c_class_id>/<str:teach_id>/t_coursestream/', views.t_course_stream, name='t_course_stream'),
    path('teacher/<str:c_class_id>/<str:teach_id>/t_post_disable_coursestream/', views.t_post_disable_course_stream, name='t_post_disable_course_stream'),
    path('teacher/<str:ques_class_id>/<str:q_user_id>/t_forpost/', views.t_forpost, name='t_forpost'),
    path('teacher/<str:ques_class_id>/<str:q_user_id>/t_postquestion/', views.t_postques, name='t_postques'),
    path('teacher/<str:q_id>/<str:u_id>/<str:p_id>/t_viewques/', views.t_viewques, name='t_viewques'),
    path('teacher/<str:q_id>/<str:u_id>/<str:p_id>/t_post_disable_viewques/', views.t_post_disable_viewques, name='t_post_disable_viewques'),
    path('teacher/<str:q_id>/<str:u_id>/<str:p_id>/t_postans/', views.t_postans, name='t_postans'),
    path('teacher/<str:u_id>/t_personalques/', views.t_personalques, name='t_personalques'),
    path('teacher/<str:u_id>/t_personalans/', views.t_personalans, name='t_personalans'),
    path('teacher/<str:a_id>/<str:u_id>/t_viewpersonalans/', views.t_viewpersonalans, name='t_viewpersonalans'),
]