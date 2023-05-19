from django.db import models


class Functionality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserActivity(models.Model):
    functionality = models.ForeignKey(Functionality, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.functionality.name}"
