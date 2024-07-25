from django.core.exceptions import ValidationError
import datetime

def validate_year(value):
    current_year = datetime.date.today().year
    if value < 1900 or value > current_year:
        raise ValidationError(f'{value} is not a valid year.')
