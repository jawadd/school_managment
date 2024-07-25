from django.db import models
from uuid import uuid4
from .validators import validate_year

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    established_year = models.IntegerField(validators=[validate_year])
    principal_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
