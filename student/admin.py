from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school', 'date_of_birth', 'email', 'phone_number', 'enrollment_date')
    list_filter = ('school', )
    search_fields = ('first_name', 'last_name', 'email')