from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='org_dashboard'),
    path('events/create/', views.create_event, name='create_event'),
]