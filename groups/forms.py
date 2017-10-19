from django import forms
from django.contrib.auth.models import User
from groups.models import Events


class EventsForm(forms.ModelForm):
    class Meta():
        model = Events
        fields = '__all__'
