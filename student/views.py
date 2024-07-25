# Views for students
from rest_framework import viewsets
from django.views.generic import ListView
from .models import  Student
from .serializers import StudentSerializer
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from django import forms


class HomeView(TemplateView):
    template_name = 'student/index.html'

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    enrollment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Student
        fields = ['school', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'enrollment_date']
class StudentList(ListView):
    model = Student
    template_name = 'student/students_list.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_queryset().exists():
            context['school'] = self.get_queryset().first().school
        return context

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

