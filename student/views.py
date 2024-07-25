# Views for students
from rest_framework import viewsets
from django.views.generic import ListView
from .models import  Student
from .serializers import StudentSerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.views.generic import CreateView
class StudentList(ListView):
    model = Student
    template_name = 'student/index.html'  # Ensure this path is correct
    context_object_name = 'students'




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# students/views.py



class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/edit_student.html'
    context_object_name = 'students'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/delete_student.html'
    context_object_name = 'students'
    success_url = reverse_lazy('student_delete')
    
    
class StudentAddView(CreateView):
    # model = Student
    # form_class = StudentForm
    # template_name = 'student/student_add.html'
    # context_object_name = 'students'
    # success_url = reverse_lazy('add_student')
    model = Student
    context_object_name = 'students'
  
    form_class = StudentForm
    template_name = 'student/student_add.html'
    success_url = reverse_lazy('student_list')
  