from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Productos

"""@receiver(post_save, sender=Productos)
def check_stock(sender, instance, **kwargs):
    if instance.stock <= instance.min_stock:
        print("El stock del producto es menor o igual al stock mínimo")
        send_mail(
            'Stock bajo en el producto {}'.format(instance.name),
            'El producto {} tiene un stock bajo. Por favor, reponer lo antes posible.'.format(instance.name),
            'spprt.slotsSolutions@gmail.com',  # Asegúrate de utilizar tu correo personalizado aquí
            ['dvs2609@gmail.com'],  # Reemplaza esto con el correo electrónico del proveedor
            fail_silently=False,
        )"""