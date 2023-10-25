from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus extra fields for CustomUser.
    """
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'surname', 'study_group', 'password1', 'password2', 'phone')
        file = forms.ImageField(
            label='Загрузите фотографию студенческого билета',
            widget=forms.FileInput(attrs={'id': 'file', 'onchange': 'displayFileName(this)'})
        )
        widgets = {
            'email': forms.EmailInput(attrs={'id': 'login', 'name': 'login', 'class': 'myemail'}),
            'study_group': forms.TextInput(attrs={'id': 'group', 'name': 'group', 'placeholder': '221-325'}),
            'first_name': forms.TextInput(attrs={'id': 'surname2', 'name': 'surname2', 'placeholder': 'Андрей'}),
            'last_name': forms.TextInput(attrs={'id': 'surname2', 'name': 'surname2', 'placeholder': 'Василиванов'}),
            'surname': forms.TextInput(attrs={'id': 'surname2', 'name': 'surname2', 'placeholder': 'Игоревич'}),
            'phone': forms.TextInput(attrs={'id': 'phone', 'name': 'phone', 'placeholder': '+7 1234567890'}),
            'password1': forms.PasswordInput(attrs={'class': 'mypassword', 'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'mypassword', 'placeholder': 'Confirm password'}),

            
            
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'id': 'login', 'name': 'login', 'class': 'myemail'})
            self.fields['study_group'].widget.attrs.update({'id': 'group', 'name': 'group', 'placeholder': '221-325'})
            self.fields['first_name'].widget.attrs.update({'id': 'surname2', 'name': 'surname2', 'placeholder': 'Андрей'})
            self.fields['last_name'].widget.attrs.update({'id': 'surname1', 'name': 'surname1', 'placeholder': 'Василиванов'})
            self.fields['surname'].widget.attrs.update({'id': 'surname3', 'name': 'surname3', 'placeholder' : 'Игоревич'})
            self.fields['phone'].widget.attrs.update({'id': 'phone', 'name': 'phone', 'placeholder': '+7 1234567890'})
            self.fields['password1'].widget.attrs.update({
                'class': 'mypassword',
            })
            self.fields['password2'].widget.attrs.update({'id': 'password', 'name': 'password', 'type': 'text'})
            
            
        
class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'study_group')
