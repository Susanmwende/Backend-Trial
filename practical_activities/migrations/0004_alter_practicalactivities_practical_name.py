# Generated by Django 5.1.1 on 2024-10-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical_activities', '0003_remove_practicalactivities_activity_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicalactivities',
            name='practical_name',
            field=models.CharField(default='Practical', max_length=100),
        ),
    ]
