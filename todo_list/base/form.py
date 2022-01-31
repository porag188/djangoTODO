
from django import forms

class InputForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()