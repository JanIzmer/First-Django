from .models import Articles
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons', 'full_text']
        
        widgets = {
              "title": TextInput(attrs={
                  'class': 'form-control',
                  'placeholder': 'Article name' 
              }),
              "anons": TextInput(attrs={
                  'class': 'form-control',
                  'placeholder': 'Anons' 
              }),
              "full_text": Textarea(attrs={
                  'class': 'form-control',
                  'placeholder': 'Article text'
              })   
        }
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    error_messages = {
        'password_mismatch': 'The passwords you entered do not match. Please try again.',
        'password_too_common': 'This password is too common. Please choose a stronger one.',
        'password_entropic': 'Your password is too simple. Please choose a more complex password.',
        'username_taken': 'This username is already taken. Please choose another one.',
        'username_required': 'Username is required. Please enter a username.',
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize individual field error messages if needed
        self.fields['username'].error_messages = {
            'required': 'Please enter a username.',
            'unique': 'This username is already taken.',
        }
        self.fields['password1'].error_messages = {
            'required': 'Please enter a password.',
            'too_common': 'This password is too common. Please choose a stronger one.',
            'password_mismatch': 'The passwords you entered do not match. Please try again.',
        }