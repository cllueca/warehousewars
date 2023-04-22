from django.db import models
from django.contrib.postgres.fields import ArrayField
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

### PRUEBAS NAZIS EN HARVARD 

class Albaranes(models.Model):
    albaran_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING)
    data = models.DateField()
    id_seguimiento = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Albaranes'


class Estados(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Estados'


class PedidoProductos(models.Model):
    product_id = models.IntegerField()
    pedido_id = models.IntegerField()
    quantity = models.IntegerField()
    total_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'PedidoProductos'


class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    date_order = models.DateField()
    status = models.ForeignKey(Estados, models.DO_NOTHING)
    total_cost = models.FloatField()
    user = models.ForeignKey('Usuarios', models.DO_NOTHING)
    address = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Pedidos'


class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    stock = models.IntegerField()
    min_stock = models.IntegerField()
    price = models.FloatField()
    location = models.CharField(max_length=25)
    image = models.ImageField(upload_to='products/')
    product_description = models.CharField(max_length=25, blank=True, null=True)
    type = models.ForeignKey('Tipos', models.DO_NOTHING)
    fecha_llegada = models.DateField(blank=True, null=True)
    arrayphotos = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Productos'


class ProveedorProducto(models.Model):
    provprod_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Usuarios', models.DO_NOTHING)
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Proveedor-Producto'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Roles'


class Tipos(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Tipos'


class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'













