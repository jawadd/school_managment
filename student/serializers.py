from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'school', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'enrollment_date']