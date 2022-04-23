from django.urls import path
from . import views

urlpatterns = [
    path('', views.contributions, name='contributions'),
    path('test_action/', views.testAction, name='test_action'),
]

