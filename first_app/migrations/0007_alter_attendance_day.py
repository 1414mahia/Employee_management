# Generated by Django 5.1.1 on 2024-10-28 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_alter_attendance_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='day',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
