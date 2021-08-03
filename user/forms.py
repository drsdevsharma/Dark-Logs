from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm , PasswordResetForm ,SetPasswordForm
from django.contrib.auth.models import User



class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
        label = 'Confirm password', 
        widget = forms.PasswordInput(attrs={'class':'form-control'})) 
    email = forms.CharField(
        label = 'Email' ,
        widget = forms.EmailInput(attrs={'class':'form-control'}))   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1','password2']
        widgets = { 'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'})
            }
        

class LoginForm(AuthenticationForm):
    """LoginForm definition."""
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(
        label = 'Password', 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))



class changePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label = 'Old Password' , 
        widget=forms.PasswordInput(attrs={'class':'form-control','autofocus':True}))
    new_password1 = forms.CharField(
        label = 'New Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(
        label = 'Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}))



class ForgotPasswordForm(PasswordResetForm):
    email = forms.CharField(
        label = 'Email',
        widget=forms.EmailInput(attrs={'class':'form-control','autofocus':True}))


class NewPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label = 'New Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(
        label = 'Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
