# Generated by Django 3.0.6 on 2020-06-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0003_tasks_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
