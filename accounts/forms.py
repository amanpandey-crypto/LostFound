from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    last_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    email = forms.EmailField(max_length=254, help_text='Required.Enter a valid email address.')
    UID = forms.CharField(max_length=20, required=True, help_text='Compulsory Field')
    Branch = forms.CharField(max_length=20, required=True, help_text='Compulsory Field')
    Year = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    ContactNo = forms.IntegerField(required=True , help_text='Compulsory Field')
    user_image = forms.URLField(required=True, help_text='Add your image file link')
    designation= forms.CharField(required=True, max_length=20)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2' )


class EditProfileForm(UserChangeForm):
    user_image = forms.URLField(required=True, help_text='Add your image file link')
    designation= forms.CharField(required=True, max_length=20)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')



