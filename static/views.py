from django.shortcuts import render
from django.db import connection, transaction
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string


# Funcion que convierte las querys a la BBDD en diccionarios, para acceder de manera mas facil al valor de cada campo en las templates
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def paginaPrincipal(request):

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "Usuarios";')
        user= dictfetchall(cursor)
        cursor.execute('SELECT * FROM "Productos";')
        product = dictfetchall(cursor)
        cursor.execute('SELECT * FROM public."Tipos";')
        tipos = dictfetchall(cursor)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()
    

    context = {'datos': user, 'producto' : product, 'conectTipo' : tipos}

    if 'queryType' in request.GET:
     context['queryType'] = request.GET['queryType']
    return render(request, 'ecommerce/inicio.html', context)




def paginaContacto(request):

    return render(request, 'ecommerce/contacto.html')

def filtroInicio(request, selectedValue):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "Productos" WHERE type_id = %s', [selectedValue])
        queryType = dictfetchall(cursor)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    data = json.dumps(queryType)
    return HttpResponse(data, content_type='application/json')