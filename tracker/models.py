from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Cycle Log Model
class CycleLog(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "date"], name="uniq_entry_per_user_per_day"),
        ]
        indexes = [models.Index(fields=["user", "-date"], name="idx_user_date_desc")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    symptom = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.symptom}"
   

# User Sheet Model
class UserSheet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sheet_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Sheet"