# Generated by Django 3.2.6 on 2021-08-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='project_screencapture',
            field=models.ImageField(blank=True, null=True, upload_to='project_screen_capture'),
        ),
    ]
