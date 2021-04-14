from django.urls import include, path

urlpatterns = [
    path('test/', include('test_service.urls')),
    path('account/', include('account_service.urls')),
]
