# Generated by Django 5.1.1 on 2024-10-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_submission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='feedback',
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='image_upload',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
