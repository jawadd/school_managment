from django.db import models
from uuid import uuid4
from .validators import validate_enrollment_date
from django.core.exceptions import ValidationError
from datetime import date
from school.models import School

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    enrollment_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def clean(self):
        super().clean()
        # Validate enrollment_date against date_of_birth
        if self.enrollment_date < self.date_of_birth:
            raise ValidationError("Enrollment date cannot be before the date of birth.")
        if self.enrollment_date > date.today():
            raise ValidationError("Enrollment date cannot be in the future.")

