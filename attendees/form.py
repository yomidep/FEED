from django import forms
from attendees.models import Attendee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = "__all__"
    
