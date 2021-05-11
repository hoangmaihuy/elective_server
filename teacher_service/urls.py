from django.urls import path

from . import views

urlpatterns = [
	path('get_teacher_list', views.get_teacher_list, name='get_teacher_list'),
]
