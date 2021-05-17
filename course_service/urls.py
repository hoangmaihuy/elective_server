from django.urls import path

from . import views

urlpatterns = [
	path('get_course_list', views.get_course_list, name='get_course_list'),
	path('get_courses_by_school', views.get_courses_by_school, name="get_courses_by_school"),
	path('get_course_rank', views.get_course_rank, name='get_course_rank'),
]
