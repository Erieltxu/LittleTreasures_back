from django.db import models
from django.contrib.auth.models import User


class Child(models.Model):
    first_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    user = models.ForeignKey(User, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name