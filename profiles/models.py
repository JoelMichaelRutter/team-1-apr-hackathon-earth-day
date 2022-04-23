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


class ProfileImage(models.Model):
    """
    Allow User to add profile image
    """
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_image')  # noqa ES501
    image = models.ImageField(upload_to='images/', blank=True)
