from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
pytestmark = pytest.mark.django_db


class AuthViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.u = User.objects.create_user(username='alice', password='pw')

    def test_submit_log_requires_login(self):
        res = self.client.post(reverse('submit_log'), data={})
        self.assertEqual(res.status_code, 302)  # redirected to login

    def test_export_requires_login(self):
        res = self.client.get(reverse('export_csv'))
        self.assertEqual(res.status_code, 302)