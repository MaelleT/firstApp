'''
Created on 15 juin 2016

@author: maelle
'''
from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta :
        model = SignUp
        fields = ['email','full_name']#fields to display
        #exclude = ['email'] not to use
        
    def clean_email(self):#checking the email data before insert  
        #print(self.cleaned_data)
        #print(self.cleaned_data.get('email'))        
        email = self.cleaned_data.get('email')
        email_base,provider = email.split("@")
        domain, extension = provider.split(".")
        if not extension =="edu" :
            raise forms.ValidationError("Please use a valid .edu email adress ")
        return email
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        #write validators
        return full_name