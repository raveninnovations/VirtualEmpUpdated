# Generated by Django 3.1.4 on 2020-12-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSM', '0017_week_unit_ucapone'),
    ]

    operations = [
        migrations.AddField(
            model_name='week_unit',
            name='uCap3',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
