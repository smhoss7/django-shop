# Generated by Django 5.0.7 on 2024-07-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(default='', max_length=300, unique=True),
        ),
    ]
