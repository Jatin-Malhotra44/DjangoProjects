# Generated by Django 3.0.1 on 2020-01-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj', '0002_anime_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='video',
            field=models.FileField(null=True, upload_to='dj/videos', verbose_name=''),
        ),
    ]