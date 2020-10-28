from django import forms

class MyForm(forms.Form):
    # Crear un <input> con un label y una restricción de 100 caracteres
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    # Crear un <input> con type=”email”
    email = forms.EmailField(label='Introduce tu email', max_length=20)

class LoginForm(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    email = forms.EmailField(label='Introduce tu email', max_length=20)