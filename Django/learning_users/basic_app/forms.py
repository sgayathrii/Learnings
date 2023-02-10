from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm): 
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
