# Generated by Django 3.0.6 on 2020-06-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0002_auto_20200616_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
