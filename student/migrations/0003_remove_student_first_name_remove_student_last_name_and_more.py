# Generated by Django 5.1.1 on 2024-10-14 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_password_student_user_name'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_name',
        ),
        migrations.AddField(
            model_name='student',
            name='school_name',
            field=models.CharField(default='AkiraChix', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
