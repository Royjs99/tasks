# Generated by Django 5.0.4 on 2024-05-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_task_task_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('usuario', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
    ]
