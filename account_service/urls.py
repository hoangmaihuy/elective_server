from django.urls import path

from . import views

urlpatterns = [
	path('request_verification_code', views.request_verification_code, name='request_verification_code'),
	path('login', views.login, name='login'),
]
