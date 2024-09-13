from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

# 알람 모델
class Alarm(models.Model):
    DAY_CHOICE = (
        ('monday', '월요일'),
        ('tuesday', '화요일'),
        ('wednesday', '수요일'),
        ('thursday', '목요일'),
        ('friday', '금요일'),
        ('saturday', '토요일'),
        ('sunday', '일요일'),
    )
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    day = MultiSelectField(choices=DAY_CHOICE)
    label = models.CharField(max_length=200)
    realert = models.BooleanField(default=True)