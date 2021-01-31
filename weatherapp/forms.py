from django import forms

class myForm(forms.Form):
    cityName=forms.CharField(max_length=25)