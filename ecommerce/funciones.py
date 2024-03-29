import datetime
from django.contrib import messages
from urllib.parse import unquote
from django import template
from urllib.parse import unquote
import re

# Funcion que convierte las querys a la BBDD en diccionarios, para acceder de manera mas facil al valor de cada campo en las templates
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        {column: (row[i].isoformat() if isinstance(row[i], datetime.date) else row[i]) for i, column in enumerate(columns)}
        for row in cursor.fetchall()
    ]


def comprobarContraseña(request, pwd, pwdConf):
    if(len(pwd) < 8):
        messages.error(request, "La contraseña debe contener al menos 8 caracteres")
        return False # longitud corta

    if(pwd != pwdConf):
        messages.error(request, "Las contraseñas no coinciden")
        return False # false
    
    return True # true

def camposObligatoriosRellenos(request, nombre, apellidos, telefono, correo, adress, cpostal):

    if len(nombre) == 0:
        messages.error(request, "Se debe dar un nombre")
        return False
    
    if len(adress) == 0:
        messages.error(request, "Se debe dar una direccion")
        return False

    if len(apellidos) == 0:
        messages.error(request, "Se debe dar un apellido")
        return False
    
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", correo):
        messages.error(request, "Introduzca un correo valido")
        return False
    
    if not re.match("[0-9]{9}", telefono):
        messages.error(request, "Introduzca un telefono valido")
        return False
    
    if not re.match("[0-9]{5}", cpostal):
        messages.error(request, "Codigo postal no valido")
        return False
    return True

register = template.Library()

@register.filter
def urldecode(value):
    return unquote(value)