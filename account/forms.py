from typing import Any
from django import forms
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# class LoginForm(forms.Form):
#     email = forms.CharField(max_length=50, required=True, label= "email", widget=forms.EmailInput(
#         attrs= {'class' : 'form-control', 'placeholder': 'Enter email'}
#     ), help_text='Required. Add a valid email address.')
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder':'Enter password',}
#     ))


class CreateUserForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1', 'password2']


class UserAuthenticationForm(AuthenticationForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password')    

    def clean(self) :
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login") 

            