from django.db import models
from django.contrib.auth.models import User


class Child(models.Model):
    user = models.ForeignKey(User, related_name='children', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name}"