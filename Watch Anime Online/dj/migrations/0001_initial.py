# Generated by Django 3.0.1 on 2020-01-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name', models.CharField(max_length=50)),
                ('anime_desc', models.CharField(max_length=300)),
                ('episodes_no', models.IntegerField()),
            ],
        ),
    ]
