from django import forms
from .models import User

class UserForm(forms.ModelForm):
    username        = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Usuario",
    )
    email           = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Correo Electrónico"
    )
    given_name      = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Nombre(s)"
    )
    first_surname   = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Apellido Paterno"
    )
    second_surname  = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Apellido Materno"
    )
    phone_number    = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class':'form-control'
        }),
        label="Número Telefónico"
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'given_name', 'first_surname', 'second_surname', 'phone_number']