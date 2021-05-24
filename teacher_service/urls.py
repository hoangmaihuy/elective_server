from django.urls import path

from . import views

urlpatterns = [
	path('get_teacher_list', views.get_teacher_list, name='get_teacher_list'),
	path('get_teachers_by_course', views.get_teachers_by_course, name='get_teachers_by_course'),
	path('get_teacher_info', views.get_teacher_info, name='get_teacher_info'),
]
