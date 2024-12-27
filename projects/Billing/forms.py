from django import forms
from .models import market,product

class marketform(forms.ModelForm):
    class Meta:
        model=market;
        fields="__all__";
class productform(forms.ModelForm):
    class Meta:
        model=product;
        fields="__all__";