# Generated by Django 5.1.1 on 2024-10-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical_activities', '0002_remove_practicalactivities_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicalactivities',
            name='activity_name',
        ),
        migrations.AddField(
            model_name='practicalactivities',
            name='grade_level',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='practicalactivities',
            name='practical_name',
            field=models.CharField(default='Unnamed Practical', max_length=100),
        ),
        migrations.AddField(
            model_name='practicalactivities',
            name='video_file',
            field=models.FileField(default='practical_videos/default_video.mp4', upload_to='practical_videos/'),
        ),
    ]
