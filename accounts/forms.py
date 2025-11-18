from django import forms

class registerform(forms.Form):
    username= forms.CharField()
    password= forms.CharField()
    gmail= forms.EmailField()

class loginform(forms.Form):
    username= forms.CharField()
    password= forms.CharField()
