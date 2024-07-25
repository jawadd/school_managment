from django.core.exceptions import ValidationError
from datetime import date

def validate_enrollment_date(value, date_of_birth):
    if value < date_of_birth:
        raise ValidationError("Enrollment date cannot be before the date of birth.")
    if value > date.today():
        raise ValidationError("Enrollment date cannot be in the future.")
