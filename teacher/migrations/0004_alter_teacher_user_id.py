# Generated by Django 5.1.1 on 2024-10-14 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_remove_teacher_first_name_remove_teacher_last_name_and_more'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user_id',
            field=models.ForeignKey(default='susan', on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
