from .models import Personal,Mark
from django import forms
class PersonalForm(forms.ModelForm):
    class Meta:
        model=Personal
        fields=['appid','name','fname','mno','email']
   
class MarkForm(forms.ModelForm):
    class Meta:
        model=Mark
        fields=['appid','m1','m2','m3','m4','m5']