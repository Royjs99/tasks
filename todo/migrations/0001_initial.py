# Generated by Django 5.0.4 on 2024-05-01 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('priority', models.CharField(max_length=50)),
            ],
        ),
    ]