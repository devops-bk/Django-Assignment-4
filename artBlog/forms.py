from django import forms

class PostForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()