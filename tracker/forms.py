from django import forms
from .models import CycleLog

# Cycle Log

SYMPTOM_CHOICES = [
    ('fatigue', 'Fatigue'),
    ('energetic', 'Energetic'),
    ('cramps', 'Cramps'),
    ('bloating', 'Bloating'),
    ('mood_swings', 'Mood Swings'),
    ('headache', 'Headache'),
    ('clear_mind', 'Clear Mind'),
]


class CycleLogForm(forms.ModelForm):
    symptom = forms.MultipleChoiceField(
        choices=SYMPTOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    notes = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CycleLog
        fields = ['date', 'symptom', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            
        }