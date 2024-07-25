from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .views import StudentList
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', StudentList.as_view(), name='student_list'),  # For rendering the student list
    
]