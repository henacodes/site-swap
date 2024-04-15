# Generated by Django 5.0.4 on 2024-04-15 14:35

import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='screenshot',
            field=models.ImageField(blank=True, max_length=255, upload_to=website.models.get_image_file_path),
        ),
    ]