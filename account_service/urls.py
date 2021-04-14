from django.urls import path

from . import views

urlpatterns = [
	path('request_auth_code', views.request_auth_code, name='request_auth_code'),
	path('login', views.login, name='login'),
]
