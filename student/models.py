from django.db import models
from uuid import uuid4
from .validators import validate_enrollment_date
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
    enrollment_date = models.DateField(validators=[validate_enrollment_date])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def clean(self):
        super().clean()
        # Validate enrollment_date against date_of_birth
        if self.enrollment_date and self.date_of_birth:
            validate_enrollment_date(self.enrollment_date, self.date_of_birth)

