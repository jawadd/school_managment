# Views for students
from rest_framework import viewsets
from django.views.generic import ListView
from .models import  Student
from .serializers import StudentSerializer

class StudentList(ListView):
    model = Student
    template_name = 'student/index.html'  # Ensure this path is correct
    context_object_name = 'students'




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

