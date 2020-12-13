from django import forms
from django.forms import ModelForm

from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'client_email',
            'topic',
        ]

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'client_email': forms.TextInput(),
            'topic': forms.TextInput(attrs={'class': 'topic_input'})

        }