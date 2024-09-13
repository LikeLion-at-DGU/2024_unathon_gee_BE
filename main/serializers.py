from rest_framework import fields, serializers
from .models import DAY_CHOICE
from .models import Alarm, AlarmSound, Fortune

class AlarmSerializer(serializers.ModelSerializer):
    day = fields.MultipleChoiceField(choices=DAY_CHOICE)
    sound = serializers.PrimaryKeyRelatedField(queryset=AlarmSound.objects.all(), required=True)

    class Meta:
        model = Alarm
        fields = ['id', 'time', 'day', 'label', 'sound']
    
class FortuneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fortune
        fields = ['id', 'content']