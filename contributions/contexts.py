"""
Importing models to extract data from db.
"""
from .models import Recycle, Reuse, Reduce


def actions_context(request):
    """
    Make action objects count available across app
    """
    recycle_objects = list(Recycle.objects.all())
    reuse_objects = list(Reuse.objects.all())
    reduce_objects = list(Reduce.objects.all())

    recycle_count = len(recycle_objects)
    reuse_count = len(reuse_objects)
    reduce_count = len(reduce_objects)

    # Specific REUSE action counts for home page
    coffee_cups = len(reuse_objects.filter(reuse_action='coffee_cups'))
    water_bottles = len(reuse_objects.filter(reuse_action='water_bottles'))
    shopping_bags = len(reuse_objects.filter(reuse_action='shopping_bags'))
    clothes = len(reuse_objects.filter(reuse_action='clothes'))
    furniture = len(reuse_objects.filter(reuse_action='furniture'))
    glass_containers = len(
        reuse_objects.filter(reuse_action='glass_containers')
    )

    # Specific REDUCE action counts for home page
    water_usage = len(reduce_objects.filter(reduce_action='water_usage'))
    car_emissions = len(reduce_objects.filter(reduce_action='car_emissions'))
    electricity_usage = len(
        reduce_objects.filter(reduce_action='electricity_usage')
    )
    natural_gas_usage = len(
        reduce_objects.filter(reduce_action='natural_gas_usage')
    )
    food_waste = len(reduce_objects.filter(reduce_action='food_waste'))
    meat_intake = len(reduce_objects.filter(reduce_action='meat_intake'))

    # Specific RECYCLE action counts for home page
    plastics = len(recycle_objects.filter(recycle_action='plastics'))
    cardboard = len(recycle_objects.filter(recycle_action='cardboard'))
    glass = len(recycle_objects.filter(recycle_action='glass'))
    metal = len(recycle_objects.filter(recycle_action='metal'))
    electronics = len(recycle_objects.filter(recycle_action='electronics'))
    organic_waste = len(recycle_objects.filter(recycle_action='organic_waste'))

    return {
        'recycle_actions': recycle_objects,
        'reuse_actions': reuse_objects,
        'reduce_actions': reduce_objects,
        'recycle_count': recycle_count,
        'reduce_count': reduce_count,
        'reuse_count': reuse_count,
        # Reuse specific action count context variables
        'coffee_cups_count': coffee_cups,
        'water_bottles_count': water_bottles,
        'shopping_bags_count': shopping_bags,
        'clothes_count': clothes,
        'furniture_count': furniture,
        'glass_containers_count': glass_containers,
        # Reduce specific action count context variables
        'water_usage_count': water_usage,
        'car_emissions_count': car_emissions,
        'electricity_usage_count': electricity_usage,
        'natural_gas_usage_count': natural_gas_usage,
        'food_waste_count': food_waste,
        'meat_intake_count': meat_intake,
        # Recycle specific action count context variables
        'plastic_recycle_count': plastics,
        'carboard_recycle_count': cardboard,
        'glass_recycle_count': glass,
        'metal_recycle_count': metal,
        'electronics_recycle_count': electronics,
        'organic_waste_recycle_count': organic_waste,
    }
