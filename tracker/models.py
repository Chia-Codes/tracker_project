from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CycleLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    symptom = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.symptom}"