from django.urls import path, include


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
