from rest_framework import serializers
from .models import Student
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = ['id', 'school', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'enrollment_date']

    def validate(self, data):
        date_of_birth = data.get('date_of_birth')
        enrollment_date = data.get('enrollment_date')

            
        if enrollment_date < date_of_birth:
            raise serializers.ValidationError("Enrollment date cannot be before the date of birth.")
        if enrollment_date > date.today():
            raise serializers.ValidationError("Enrollment date cannot be in the future.")
        if date_of_birth > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")

        
        return data