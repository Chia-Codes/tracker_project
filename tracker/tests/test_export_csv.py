from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tracker.models import CycleLog
from datetime import date
import csv
import io
import pytest
pytestmark = pytest.mark.django_db


class ExportCsvTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.u1 = User.objects.create_user(username='alice', password='pw')
        self.u2 = User.objects.create_user(username='bob', password='pw')
        # alice logs
        CycleLog.objects.create(user=self.u1, date=date(2025, 9, 25), symptom='cramps', notes='n1')
        CycleLog.objects.create(user=self.u1, date=date(2025, 9, 24), symptom='headache', notes='')
        # bob log (same day as alice to ensure filtering works)
        CycleLog.objects.create(user=self.u2, date=date(2025, 9, 25), symptom='fatigue', notes='x')

    def test_requires_login(self):
        res = self.client.get(reverse('export_csv'))
        # Not logged in → redirect to login
        self.assertEqual(res.status_code, 302)

    def test_exports_only_logged_in_users_rows(self):
        self.client.login(username='alice', password='pw')
        res = self.client.get(reverse('export_csv'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['Content-Type'], 'text/csv')
        self.assertIn('attachment; filename="trackher_entries.csv"', res['Content-Disposition'])

        content = res.content.decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        rows = list(reader)
        # header + 2 rows for alice
        self.assertGreaterEqual(len(rows), 3)
        self.assertEqual(rows[0], ['date', 'symptom', 'notes'])
        data_rows = rows[1:]
        # Should contain alice's symptoms, not bob's
        flat = ''.join(','.join(r) for r in data_rows)
        self.assertIn('cramps', flat)
        self.assertIn('headache', flat)
        self.assertNotIn('fatigue', flat)  # bob's symptom should be absent
        self.assertNotIn('x', flat)        # bob's notes should be absent