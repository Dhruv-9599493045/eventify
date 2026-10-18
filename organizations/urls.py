from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='org_dashboard'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),
    path('events/<int:event_pk>/add-session/', views.add_session, name='add_session'),
    path('events/<int:event_pk>/managers/', views.assign_manager, name='assign_manager'),
    path('managers/<int:assignment_pk>/remove/', views.remove_manager, name='remove_manager'),
]