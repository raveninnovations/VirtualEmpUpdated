# Generated by Django 3.1.4 on 2020-12-13 08:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_id', models.IntegerField(default=0)),
                ('create_category', models.CharField(max_length=255, null=True)),
                ('create_sub', models.CharField(max_length=255, null=True)),
                ('create_course', models.CharField(max_length=255)),
                ('create_instructor', models.CharField(max_length=255, null=True)),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('title', models.CharField(max_length=50)),
                ('tagline', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='csm_images/')),
                ('category', models.CharField(blank=True, choices=[('IT', 'IT & Software'), ('Business & Startups', 'Business & Startups'), ('Designing', 'Designing'), ('Electronics & Electricals', 'Electronics & Electricals')], max_length=30, null=True)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('course', models.CharField(blank=True, max_length=50)),
                ('difficulty_level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20, null=True)),
                ('instructor', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keywords', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('course_points', models.IntegerField(default=0)),
                ('certificate', models.CharField(blank=True, max_length=200, null=True)),
                ('requirements', models.TextField(blank=True)),
                ('learnings', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
