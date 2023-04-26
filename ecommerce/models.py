from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from phonenumber_field.validators import ValidationError
# validate_international_phonenumber por ahora no se usa tengo que ver como hacerlo para poner la extension sin que de error.
class User(AbstractUser):

    # null true = la BBDD puede tener este campo vacio
    # blank true = se puede dejar vacio en el formulario
    email = models.EmailField(unique=True) # con esto se indica que el login sea con email, ya no se pueden repetir
    telefono = models.CharField(max_length=15, validators=[ValidationError], null=True, blank=True)
    adress = models.CharField(max_length=250, null=True, blank=True)
    cpostal = models.CharField(max_length=10, null=True, blank=True)
    role_id = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Transportistas(models.Model):
    id_trans = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'Transportistas'

class Albaranes(models.Model):
    albaran_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey('Pedidos', on_delete=models.CASCADE)
    date = models.DateField()
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


class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    date_order = models.DateField()
    status = models.ForeignKey(Estados,on_delete=models.CASCADE)
    total_cost = models.FloatField()
    user= models.ForeignKey('User',on_delete=models.CASCADE)
    address = models.CharField(max_length=25)
    cpostal = models.CharField(max_length=10)
    total_weight =  models.FloatField()
    isUrgent = models.BooleanField()
    transportista = models.ForeignKey(Transportistas,on_delete=models.CASCADE)
    arrival_date = models.DateField()
    total_products = models.IntegerField()

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
    type = models.ForeignKey('Tipos',on_delete=models.CASCADE)
    fecha_llegada = models.DateField(blank=True, null=True)
    weight = models.FloatField()
    isRestock = models.BooleanField()


    class Meta:
        managed = False
        db_table = 'Productos'

class PedidoProductos(models.Model):
    product_id = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column='product_id')  
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='pedido_id')
    quantity = models.IntegerField()
    total_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'PedidoProductos'

class ProveedorProducto(models.Model):
    provprod_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
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
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'

