from django.template import Library
from django import template
from urllib.parse import unquote
from decimal import Decimal

register=Library()

@register.filter
def urldecode(value):
    return unquote(value)

@register.filter
def total_price(cart_items):
    total = Decimal(0)

    if len(cart_items) != 0:
        for item in cart_items.values():
            price = Decimal(item['price'])
            quantity = item['quantity']
            total += price * quantity
        return total
    else:
        return 0