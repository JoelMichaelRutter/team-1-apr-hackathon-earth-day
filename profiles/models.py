from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Maintain User Profile history
    Log of contributions
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
