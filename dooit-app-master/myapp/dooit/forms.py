from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Insert password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='first_name',widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'placeholder':'Insert password'}))
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'placeholder':'Insert password again'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

from . models import Transaksi

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = "__all__"