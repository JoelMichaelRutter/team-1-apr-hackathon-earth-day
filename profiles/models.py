from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class UserProfile(models.Model):
    """
    Maintain User Profile history
    Log of contributions
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='/images/earth_solid.png')  # noqa ES501

    def __str__(self):
        return self.user.username

    # resizing images
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         new_img = (300, 300)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)
