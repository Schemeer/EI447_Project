from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=255, widget=forms.TextInput(attrs={'class': 'text'}))
    password = forms.CharField(label="Password", max_length=255, widget=forms.PasswordInput(attrs={'class': 'text'}))

class RegistForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=255, widget=forms.TextInput(attrs={'class': 'text'}))
    password1 = forms.CharField(label="Password", max_length=255, widget=forms.PasswordInput(attrs={'class': 'text'}))
    password2 = forms.CharField(label="Confirm Password", max_length=255, widget=forms.PasswordInput(attrs={'class': 'text'}))
