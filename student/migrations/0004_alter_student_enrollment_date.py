# Generated by Django 5.0.7 on 2024-07-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_enrollment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment_date',
            field=models.DateField(),
        ),
    ]