from django import forms

from .models import Customer

class CustomerForm(forms.ModelForm):
    class meta:
        model = Customer
        fields = '__all__'
