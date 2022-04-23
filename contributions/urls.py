from django.urls import path
from . import views

urlpatterns = [
    path('contribute/', views.contributions, name='contribute'),
]
