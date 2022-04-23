from django.db import models
from profiles.models import UserProfile

class Reuse(models.Model):
    """
    Allow user to choose which type of Reuse action to contribute
    """
    REUSE_TYPES = (
        ('coffee_cups', 'coffee_cups',),
        ('water_bottles', 'water_bottles',),
        ('shopping_bags', 'shopping_bags',),
        ('clothes', 'clothes',),
        ('furniture', 'furniture',),
        ('glass_containers', 'glass_containers',),
        ('other', 'other',),
    )

    action = models.CharField(
        max_length=50,
        choices=REUSE_TYPES,
        default=None
    )
    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reuse_actions')  # noqa ES501
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} contributed by {self.profile}'


class Reduce(models.Model):
    """
    Allow user to choose which type of Reduce action to contribute
    """
    REDUCE_TYPES = [
        ('water_usage', 'water_usage',),
        ('car_emissions', 'car_emissions',),
        ('electricity_usage', 'electricity_usage',),
        ('natural_gas_usage', 'natural_gas_usage',),
        ('food_waste', 'food_waste',),
        ('meat_intake', 'meat_intake',),
    ]

    action = models.CharField(
        max_length=50,
        choices=REDUCE_TYPES,
        default=None
    )
    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reduce_actions')  # noqa ES501
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} contributed by {self.profile}'


class Recycle(models.Model):
    """
    Allow user to choose which type of Recycle action to contribute
    """
    RECYCLE_TYPES = [
        ('plastics', 'plastics',),
        ('cardboard', 'cardboard',),
        ('glass', 'glass',),
        ('metal', 'metal',),
        ('electronics', 'electronics',),
        ('organic_waste', 'organic_waste',),
    ]

    action = models.CharField(
        max_length=50,
        choices=RECYCLE_TYPES,
        default=None
    )
    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='recycle_actions')  # noqa ES501
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} contributed by {self.profile}'
