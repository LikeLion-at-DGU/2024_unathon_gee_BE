from rest_framework import fields, serializers
from .models import DAY_CHOICE
from .models import Alarm

class AlarmSerializer(serializers.ModelSerializer):
    day = fields.MultipleChoiceField(choices=DAY_CHOICE)
    class Meta:
        model = Alarm
        fields = ['id', 'time', 'day', 'label', 'realert']