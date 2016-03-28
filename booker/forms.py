from django import forms
from django.contrib.auth.models import User
from booker.models import Application, Booking, Market, Stall, UserProfile

class ApplicationForm(forms.ModelForm):
    
    
    class Meta:
        model = Application
        fields = ('stall','market')