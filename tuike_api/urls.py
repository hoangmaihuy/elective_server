from django.urls import include, path

urlpatterns = [
    path('test/', include('test_service.urls')),
    path('account/', include('account_service.urls')),
    path('course/', include('course_service.urls')),
    path('review/', include('review_service.urls')),
]
