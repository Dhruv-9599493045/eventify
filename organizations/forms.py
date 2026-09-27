from django import forms
from events.models import Event,Session

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'banner_image', 'venue', 'start_date', 'end_date', 'category', 'status']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'speaker', 'venue', 'start_time', 'end_time', 'capacity']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }