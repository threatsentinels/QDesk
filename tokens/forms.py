from django import forms 
from .models import Organization 


class Organization(forms.ModelForm):
    class Meta:
        model = Organization 
        fields = ["name","logo"]
        