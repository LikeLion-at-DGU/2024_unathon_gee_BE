from django.contrib import admin
from .models import AlarmSound, Alarm, Fortune

@admin.register(AlarmSound)
class AlarmSoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    search_fields = ('name',)

@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = ('label', 'time', 'get_days', 'sound')
    list_filter = ('sound',)
    search_fields = ('label',)

    def get_days(self, obj):
        return ", ".join(obj.day)
    get_days.short_description = 'Days'
    

admin.site.register(Fortune)