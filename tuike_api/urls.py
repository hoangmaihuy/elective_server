from django.urls import include, path

urlpatterns = [
    path('test/', include('test_service.urls')),
    path('account/', include('account_service.urls')),
    path('course/', include('course_service.urls')),
    path('review/', include('review_service.urls')),
    path('teacher/', include('teacher_service.urls')),
]
