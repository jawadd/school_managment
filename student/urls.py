from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentList, StudentCreate, StudentUpdate, StudentDelete
from .views import StudentList,HomeView
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('students/', StudentList.as_view(), name='student_list'),
    path('create/', StudentCreate.as_view(), name='student_create'),
    path('update/<uuid:pk>/', StudentUpdate.as_view(), name='student_update'),
    path('delete/<uuid:pk>/', StudentDelete.as_view(), name='student_delete'),
    
]
