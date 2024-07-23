from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             validators=[validators.validate_email
                                 , validators.MaxLengthValidator(254),
                                         validators.MinLengthValidator(8), ])

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               validators=[
                                   validators.MaxLengthValidator(100), validators.MinLengthValidator(8),

                               ])

    confirm_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(8),
        ])

    def clean_confirm_pass(self):
        password=self.cleaned_data['password']
        confirm_pass=self.cleaned_data['confirm_pass']
        if password != confirm_pass:
            raise forms.ValidationError('Passwords must match')

        else:
            return confirm_pass;


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             validators=[validators.validate_email
                                 , validators.MaxLengthValidator(254),
                                         validators.MinLengthValidator(8), ])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               validators=[
                                   validators.MaxLengthValidator(100), validators.MinLengthValidator(8),

                               ])


class ForgotForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               validators=[
                                   validators.MaxLengthValidator(100), validators.MinLengthValidator(8),

                               ])

    confirm_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(8),
        ])
