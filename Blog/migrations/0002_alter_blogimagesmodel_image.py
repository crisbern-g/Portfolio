# Generated by Django 3.2.6 on 2021-08-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimagesmodel',
            name='image',
            field=models.ImageField(upload_to='blog_images'),
        ),
    ]
