from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]