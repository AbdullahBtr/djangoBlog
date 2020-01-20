from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text=None
            
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['password1'].widget.attrs['placeholder'] = '8 characters atleast'
        self.fields['password2'].widget.attrs['placeholder'] = 'repeat password'


    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
        
        

class CustomUserChangeForm(UserChangeForm):
    model=CustomUser
    fields=('email','password1','password2')    



class RegistrationFormUniqueEmail(CustomUserCreationForm):
  
    def clean_email(self):

        if CustomUser.objects.filter(email__iexact=self.cleaned_data['email']):
            raise ValidationError(" Email address is already in use")
        return self.cleaned_data['email']




#not used yet
class CustomUserCreationFormNoTrashEmail(CustomUserCreationForm):
    """
    Subclass of ``CustomUserCreationForm`` which disallows registration with
    email addresses from trash mail webservices.
    """
    trash_domains = ['trashmail.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known trash mail services.
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.trash_domains:
            raise ValidationError("Registration using free email addresses is prohibited. Please supply a different email address.")
        return self.cleaned_data['email']         