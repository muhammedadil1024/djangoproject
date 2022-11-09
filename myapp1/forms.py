from django import forms
from django.forms import ClearableFileInput, EmailInput, NumberInput, TextInput
from .models import Gallery, RegTable

# Register form
class RegisterForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "form-control", 'style' : 'max-width: 300px; margin-left: 76px;', 'placeholder' : 'Password'}),max_length=8,min_length=2)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "form-control", 'style' : 'max-width: 300px; margin-left: 76px;', 'placeholder' : 'Confirm Password'}),max_length=8,min_length=2)

    class Meta():
        model = RegTable
        fields = '__all__'
        widgets = {
            'Name' : TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;',
                'placeholder' : 'Name' 
            }),
            'Age' : NumberInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;',
                'placeholder' : 'Age'
            }),
            'Place' : TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;',
                'placeholder' : 'Place'
            }),
            'Photo' : ClearableFileInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;'
            }),
            'Email' : EmailInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;',
                'placeholder' : 'Email'
            })
                                                         #FileInput-img/ClearableFileInp
                                                                               #NumberInp
        }


# Login form
class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'style' : 'max-width: 300px; margin-left: 76px;', 'placeholder' : 'Password'}),max_length=8,min_length=2)

    class Meta():
        model = RegTable
        fields = ('Email','Password')
        widgets = {
            'Email' : EmailInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 76px;',
                'placeholder' : 'Email'
            })
        }


# Change Password
class ChangePassForm(forms.Form):
    OldPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'style' : 'max-width: 300px; margin-left: 8rem', 'placeholder' : 'Old Password'}),max_length=8,min_length=2)    
    NewPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'style' : 'max-width: 300px; margin-left: 8rem', 'placeholder' : 'New Password'}),max_length=8,min_length=2)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'style' : 'max-width: 300px; margin-left: 8rem', 'placeholder' : 'Confirm Password'}),max_length=8,min_length=2)


# Update form
class UpdateForm(forms.ModelForm):

    class Meta():
        model = RegTable
        fields = ('Name','Age','Place','Email')
        widgets = {
            'Name' : TextInput(attrs={
                'class' : "form-control",
                'style' : 'width: 300px; margin-left: 8rem;',
                'placeholder' : 'Name' 
            }),
            'Age' : NumberInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 8rem;',
                'placeholder' : 'Age'
            }),
            'Place' : TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 8rem;',
                'placeholder' : 'Place'
            }),
            'Email' : EmailInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px; margin-left: 8rem;',
                'placeholder' : 'Email'
            })
        }    


# Image Galler
class Image(forms.ModelForm):

    class Meta():
        model = Gallery
        fields = '__all__'