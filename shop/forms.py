from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from .models import Customer

class NewUserForm(UserCreationForm):
    username = forms.CharField(
                label= ("Enter your Name"),
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
                label= ("Enter Email Address"),
                widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'})
    )
    password1 = forms.CharField(
                label= ("Password"),
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
                label= ("Confirm Password"),
                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomerProfile(forms.ModelForm):
    name = forms.CharField(
                label= ("Your Name"),
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    address = forms.CharField(
                label= ("Adress"),
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
    )
    city = forms.CharField(
                label= ("City"),
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your City'})
    )
    state = forms.CharField(
                label= ("State"),
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'})
    )
    zipcode = forms.IntegerField(
                label= ("zipcode"),
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'})
    )
    class Meta:
        model = Customer
        fields = ["name", "address", "city", "state", "zipcode"]