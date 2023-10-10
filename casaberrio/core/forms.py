from django import forms
from .models import Register

class formularioRegistro(forms.ModelForm):
    class Meta:
        model = Register  
        fields = ['name', 'lastname', 'username', 'phone', 'email', 'password', 'confirm_password']