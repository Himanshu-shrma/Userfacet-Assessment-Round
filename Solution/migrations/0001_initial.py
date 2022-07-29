# Generated by Django 4.0.6 on 2022-07-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scheduled_classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Student Name')),
                ('class_date', models.DateField(verbose_name='Scheduled Date')),
                ('teacher_name', models.CharField(max_length=50, verbose_name='Teacher Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Student Email')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('weekday', models.CharField(max_length=50, verbose_name='Day')),
            ],
        ),
    ]
