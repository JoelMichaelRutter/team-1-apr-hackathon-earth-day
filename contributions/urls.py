from django.urls import path
from . import views

urlpatterns = [
    path('contribute/', views.contributions, name='contribute'),
    path('add_recycle/', views.add_recycle, name='add_recycle'),
    path('add_reduce/', views.add_reduce, name='add_reduce'),
    path('add_reuse/', views.add_reuse, name='add_reuse'),
]
