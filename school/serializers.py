from rest_framework import serializers
from .models import School
import datetime
from .validators import validate_year
# Custom validator for year

class SchoolSerializer(serializers.ModelSerializer):
    established_year = serializers.IntegerField(validators=[validate_year])

    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'phone_number', 'email', 'established_year', 'principal_name']
