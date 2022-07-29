from calendar import weekday
from django.db import models



# Create your models here.
class scheduled_classes(models.Model):
    name=models.CharField('Student Name',max_length=50)
    class_date=models.DateField('Scheduled Date')
    teacher_name=models.CharField('Teacher Name',max_length=50)
    email=models.EmailField('Student Email')
    start_time=models.TimeField('Start Time')
    end_time=models.TimeField('End Time')
    weekday=models.CharField('Day', max_length=50)

