from django.db import models
from django.contrib.sessions.models import Session


class Functionality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserActivity(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    functionality = models.ForeignKey(Functionality, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session.session_key} - {self.functionality.name}"
