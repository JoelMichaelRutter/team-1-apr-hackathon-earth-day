from django.urls import path
from . import views

urlpatterns = [
    path('', views.testAction, name='contributions'),
]