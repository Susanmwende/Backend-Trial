# Generated by Django 5.1.1 on 2024-10-13 08:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical_activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicalactivities',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='practicalactivities',
            name='submission_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
