from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from phonenumber_field.validators import ValidationError, validate_international_phonenumber
# validate_international_phonenumber por ahora no se usa tengo que ver como hacerlo para poner la extension sin que de error.


class User(AbstractUser):

    # null true = la BBDD puede tener este campo vacio
    # blank true = se puede dejar vacio en el formulario

    email = models.EmailField(unique=True) # con esto se indica que el login sea con email, ya no se pueden repetir
    telefono = models.CharField(max_length=15, validators=[ValidationError], null=True, blank=True)#PhoneField(blank=True, null=True)
    adress = models.CharField(max_length=250, null=True, blank=True)
    role_id = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
