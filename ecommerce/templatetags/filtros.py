from django.template import Library
from django import template
from urllib.parse import unquote
from decimal import Decimal
from ecommerce.models import Albaranes, Productos

register=Library()

@register.filter
def urldecode(value):
    return unquote(value)

@register.filter
def total_price(cart_items , value):
    total = Decimal(0)
    if len(cart_items) != 0:
        for item in cart_items.values():
            price = Decimal(item['price'])
            quantity = item['quantity']
            total += price * quantity

        if(value):
            return total + Decimal(5.75)
        else:
            return total
    else:
        return 0
    

@register.filter
def get_stock(product_id):
    product = Productos.objects.get(pk=product_id)
    return product.stock

@register.filter
def get_albaran(pedido_id):
    return Albaranes.objects.filter(pedido_id=pedido_id).exists()