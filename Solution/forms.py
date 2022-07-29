from django.forms import ModelForm
from .models import scheduled_classes

class StudentSlotForm(ModelForm):
    class Meta:
        model= scheduled_classes
        fields= ('name','email','weekday','start_time','end_time')
        labels={
            'name' : 'Student Name', 
            'email':'Email',
            'weekday':'Weekday',
            'start_time':'Start Time',
            'end_time':'End Time'
        }