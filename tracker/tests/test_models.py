from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import date
from tracker.models import CycleLog
import pytest
pytestmark = pytest.mark.django_db


class CycleLogModelTests(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(username='alice', password='pw')

    def test_unique_per_user_per_day(self):
        CycleLog.objects.create(user=self.u, date=date(2025, 9, 25), symptom='cramps', notes='')
        with self.assertRaises(IntegrityError):
            CycleLog.objects.create(user=self.u, date=date(2025, 9, 25), symptom='headache', notes='x')