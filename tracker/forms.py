from django import forms
from .models import CycleLog

# Cycle Log


class CycleLogForm(forms.ModelForm):
    class Meta:
        model = CycleLog
        fields = ['date', 'symptom', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }