# Generated by Django 3.1.4 on 2020-12-19 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0006_week_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='hello',
        ),
    ]