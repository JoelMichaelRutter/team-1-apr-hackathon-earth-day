from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Maintain User Profile history
    Log of contributions
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='/images/earth_solid.png')  # noqa ES501

    def __str__(self):
        return self.user.username
