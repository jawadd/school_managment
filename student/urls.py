from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .views import StudentList
from . import views
from .views import StudentListView, StudentUpdateView, StudentDeleteView,StudentAddView

router = DefaultRouter()
router.register(r'student', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', StudentList.as_view(), name='student_list'),  # For rendering the student list
    path('', StudentListView.as_view(), name='student_list'),
    path('<uuid:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('<uuid:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('<uuid:pk>/add/', StudentAddView.as_view(), name='student_add'),
    
]