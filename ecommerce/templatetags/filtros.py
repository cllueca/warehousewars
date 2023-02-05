from django.template import Library

register=Library()

def add_class(campo, className):
    return campo.as_widget(attrs={"class": className})

register.filter("addClass", add_class)