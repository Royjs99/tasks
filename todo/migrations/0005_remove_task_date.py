# Generated by Django 5.0.4 on 2024-05-01 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]