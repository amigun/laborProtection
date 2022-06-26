from django import forms
from .models import *

class WebPassport(forms.ModelForm):
    class Meta:
        model = ModelOrganization
        fields = '__all__'