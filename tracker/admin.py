from django.contrib import admin
from .models import CycleLog

# Register your models here.


@admin.register(CycleLog)
class CycleLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'symptom')
    list_filter = ('user', 'date')
    search_fields = ('symptom', 'notes')