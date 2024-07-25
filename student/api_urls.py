# student/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from school.views import SchoolViewSet

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'schools', SchoolViewSet, basename='school')

urlpatterns = [
    path('', include(router.urls)),
]
