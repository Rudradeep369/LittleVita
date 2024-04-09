from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import VaccineStatus, Child
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control input', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control input', 'placeholder': 'Re-enter Password'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'input','placeholder': 'Enter your Phone Number'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']   
        labels = {
            'username':'Username',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'phone_number':'Phone Number',
        }     

        widgets ={
            'username':forms.TextInput(attrs={'id':'form-input1', "class":'input', 'placeholder': 'Enter your Username'}),
            'first_name':forms.TextInput(attrs={'id':'id_fname', "class":'input', 'placeholder': 'Enter your First Name'}),
            'last_name':forms.TextInput(attrs={'id':'id_lname', "class":'input', 'placeholder': 'Enter your Last Name'}),
            'email':forms.TextInput(attrs={'id':'id_email', "class":'input', 'placeholder': 'Enter your Email Address'}),
            # 'phone_number':forms.TextInput(attrs={'id':'id_phone', "class":'input', 'placeholder': 'Enter your Phone Number'}),
        }

class VaccineStatusForm(forms.ModelForm):
    hidden_field = forms.CharField(widget=forms.HiddenInput(), initial='vaccine_status', required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(VaccineStatusForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['child'].queryset = Child.objects.filter(parent=user)

    class Meta:
        model = VaccineStatus
        fields = ['child', 'vaccine', 'completed' , 'date_of_vaccination']
        labels = {
            'child':'Child',
            'completed':'Completed',
            'vaccine':'Vaccine',
            'date_of_vaccination':'Date of Vaccination',
        }
        widgets = {
            "child":forms.Select(attrs={'class':'vaccine-form-input'}),
            "vaccine":forms.Select(attrs={'class':'vaccine-form-input'}),
            'completed':forms.CheckboxInput(attrs={'class':'vaccine-form-input'}),
            'date_of_vaccination':forms.DateInput(attrs={'class':'vaccine-form-input', 'type': 'date'}),
        }


# Overrider the AuthenticationForm 
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter your Password'}))