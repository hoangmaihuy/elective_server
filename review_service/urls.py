from django.urls import path

from . import views

urlpatterns = [
    path('add_review', views.add_review, name='add_review'),
    path('get_latest_reviews', views.get_latest_reviews, name='get_latest_reviews'),
    path('get_course_reviews', views.get_course_reviews, name='get_course_reviews'),
    path('interact_review', views.interact_review, name='interact_review'),
]
