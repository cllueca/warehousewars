from django.shortcuts import render
from django.db import connection, transaction


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
        data = dictfetchall(cursor)
    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()
    

    context = {'datos': data}
    return render(request, 'ecommerce/inicio.html', context)