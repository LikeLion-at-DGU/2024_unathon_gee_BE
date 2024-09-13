from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
DAY_CHOICE = (
    ('monday', 'monday'),
    ('tuesday', 'tuesday'),
    ('wednesday', 'wednesday'),
    ('thursday', 'thursday'),
    ('friday', 'friday'),
    ('saturday', 'saturday'),
    ('sunday', 'sunday'),
)

# 알람사운드
class AlarmSound(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='alarm_sounds/')
    
    def __str__(self):
        return self.name

# 알람 모델
class Alarm(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    day = MultiSelectField(choices=DAY_CHOICE)
    label = models.CharField(max_length=200)
    sound = models.ForeignKey(AlarmSound, on_delete=models.CASCADE, default=1)
    # realert = models.BooleanField(default=True)
    
# 운세 모델
class Fortune(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)