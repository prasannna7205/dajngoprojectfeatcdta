from django import forms
from featchapp.models import employees
class users(forms.ModelForm):
    class Meta:
        model=employees
        fields='__all__'
