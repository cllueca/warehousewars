from django.shortcuts import render, redirect
from django.db import connection, transaction
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from ecommerce.models import User
from .funciones import *


def paginaPrincipal(request):

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "Usuarios";')
        user= dictfetchall(cursor)
        cursor.execute('SELECT * FROM "Productos";')
        product = dictfetchall(cursor)
        cursor.execute('SELECT * FROM "Tipos";')
        tipos = dictfetchall(cursor)
        cursor.execute('SELECT * FROM "Usuarios" WHERE role_id = 2;')
        proveedor = dictfetchall(cursor)

        showmore = 3

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()
    context = {'datos': user, 'producto' : product, 'conectTipo' : tipos,'conectProveedor' : proveedor,}
    return render(request, 'ecommerce/inicio.html', context)


def descripcionProducto(request, productId):

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "Productos" WHERE product_id = %s ',[productId])
        productosDesc = dictfetchall(cursor)
        print(productosDesc)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    context = {'productosDesc' : productosDesc}
    return render(request, 'ecommerce/descProducto.html', context)


def paginaContacto(request):

    return render(request, 'ecommerce/contacto.html')


def filtroInicio(request, selectedValue):
    try:
        cursor = connection.cursor()
        if(selectedValue == 0):
            cursor.execute('SELECT * FROM "Productos";')
        else:
            cursor.execute('SELECT * FROM "Productos" WHERE type_id = %s', [selectedValue])
        queryType = dictfetchall(cursor)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    data = json.dumps(queryType)
    return HttpResponse(data, content_type='application/json')


def filtroPrecio(request, selectedPrize):
    try:
        cursor = connection.cursor()
        if(selectedPrize == 0):
            cursor.execute('SELECT * FROM "Productos" ORDER BY name DESC;')
        elif(selectedPrize == 1):
            cursor.execute('SELECT * FROM "Productos" ORDER BY cost_per_unit ASC;')
        else:
            cursor.execute('SELECT * FROM "Productos" ORDER BY cost_per_unit DESC;')
        queryType = dictfetchall(cursor)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    data = json.dumps(queryType)
    return HttpResponse(data, content_type='application/json')


def filtroProveedor(request, selectedProveedor):
    try:
        
        cursor = connection.cursor()
        if(selectedProveedor == 0):
            cursor.execute('SELECT * FROM "Productos";')
        else:
            cursor.execute('SELECT * FROM "Proveedor-Producto" JOIN "Usuarios" ON "Usuarios".user_id = "Proveedor-Producto".user_id JOIN "Productos" ON "Productos".product_id = "Proveedor-Producto".product_id WHERE "Usuarios".user_id = %s', [selectedProveedor])        
            queryType = dictfetchall(cursor)

    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    data = json.dumps(queryType)
    return HttpResponse(data, content_type='application/json')


def iniciarSesion(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get("password")

        try: # check if the user exists
            user = User.objects.get(username=username)
            print("YAY")
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Username or password does not exist')

    return render(request, 'ecommerce/login.html')


def registrarse(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        pwd = request.POST.get('password')
        pwdConf = request.POST.get('password2')

        if(comprobarContraseña(pwd, pwdConf) == 1): # funcion un poco basica, mejorar mas adelante

            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=pwd,
                first_name=request.POST.get('username'),
                last_name=request.POST.get('apellidos'),
                email=request.POST.get('correo'),
                telefono=request.POST.get('telefono'),
                role_id=2,
            )

            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'ecommerce/register.html')


def logoutUser(request):
    logout(request)
    return redirect('home')