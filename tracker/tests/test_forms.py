from django.test import TestCase
from tracker.forms import CycleLogForm


class CycleLogFormTests(TestCase):
    def test_clean_symptom_joins_list(self):
        form = CycleLogForm(data={'date': '2025-09-25', 'symptom': ['cramps', 'headache'], 'notes': ''})
        form.is_valid()
        self.assertEqual(form.cleaned_data.get('symptom'), 'cramps,headache')