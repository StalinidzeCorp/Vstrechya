# Generated by Django 5.0.3 on 2024-05-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='slug',
            field=models.SlugField(max_length=128, null=True, unique=True),
        ),
    ]