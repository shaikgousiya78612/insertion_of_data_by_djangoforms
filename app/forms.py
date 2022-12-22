from django import forms


class SchoolForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Principal=forms.CharField(max_length=100)
    Location=forms.CharField(max_length=100)