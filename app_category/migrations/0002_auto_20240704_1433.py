# Generated by Django 3.1 on 2024-07-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
