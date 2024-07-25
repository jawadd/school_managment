from django.core.exceptions import ValidationError
from .models import Student
import datetime

def validate_year(value):
    current_year = datetime.date.today()
    if value > current_year or value enrollment_date:
        raise ValidationError(f'{value} is not a valid year.')
