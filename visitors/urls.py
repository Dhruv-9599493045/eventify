from django.urls import path
from . import views

urlpatterns = [
    path('register/<int:pk>/', views.register_for_event, name='register_for_event'),
    path('my-registrations/', views.my_registrations, name='my_registrations'),
    path('qr/<uuid:badge_id>/', views.registration_qr, name='registration_qr'),
]