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
# 알람 모델
class Alarm(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    day = MultiSelectField(choices=DAY_CHOICE)
    label = models.CharField(max_length=200)
    # realert = models.BooleanField(default=True)