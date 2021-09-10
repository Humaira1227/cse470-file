from django import forms
from django.forms.forms import Form
class ProductView(forms.Form) :
    item= forms.CharField()
