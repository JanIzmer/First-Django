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