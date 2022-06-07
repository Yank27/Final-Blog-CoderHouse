from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#-----------------------------------------------------------------------------------------------------------------------------------------------

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
       
class UserUpdateForm(UserCreationForm):
    first_name= forms.CharField(label="Edit name", required=True)
    last_name= forms.CharField(label="Edit lastname", required=True)
    email= forms.EmailField(required=True)
    image = forms.ImageField(label="Edit avatar", required=False)
    class Meta:
        model = UserUpdate
        fields = ('first_name','last_name', 'email')
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField(label="Avatar")
