from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    date_applied = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company}-{self.role}"


