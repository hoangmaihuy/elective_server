from django.urls import path

from . import views

urlpatterns = [
	path('get_course_list', views.get_course_list, name='get_course_list'),
]
