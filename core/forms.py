from django import forms
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#La clase Meta se utiliza para proporcionar metadatos adicionales sobre un modelo. 
#Metadatos: Son datos sobre los datos. En Django, son configuraciones o información adicional que se 
#   aplica al modelo sin ser parte directamente de los campos o métodos del modelo.

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = "nombre", "correo", "tipo_consulta", "mensaje", "avisos"  (Manual)
        fields = '__all__' #Para todos los datos del modelo