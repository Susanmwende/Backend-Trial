# Generated by Django 5.1.1 on 2024-10-08 08:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('practical_activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default='Default description', max_length=255)),
                ('due_date', models.DateField()),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('practical_activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practical_activities.practicalactivities')),
            ],
        ),
    ]
