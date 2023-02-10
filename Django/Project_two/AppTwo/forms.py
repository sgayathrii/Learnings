from django import forms 
from AppTwo.models import User_data

#create the actual class
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User_data
        fields = '__all__'