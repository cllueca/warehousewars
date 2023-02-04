from django.forms import ModelForm
from .models import User

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        #fields = '__all__'  # Crearia el formulario con todos los campos editables de la tabla Room
        # se pueden excluir valores o poner solo los necesarios
        fields = ['first_name', 'last_name', 'email', 'password'] # meter el telefono tambien