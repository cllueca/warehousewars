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
from django.contrib import messages
from .forms import UserCreationForm


def paginaPrincipal(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        return render(request, 'ecommerce/vistaAlmacen.html')
    else:
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM "Usuarios";')
            user= dictfetchall(cursor)
            cursor.execute(f'SELECT * FROM "Productos" LIMIT 6;')
            product = dictfetchall(cursor)
            cursor.execute('SELECT * FROM "Productos" LIMIT 4;')
            productCarrousel = dictfetchall(cursor)
            cursor.execute('SELECT * FROM "Tipos";')
            tipos = dictfetchall(cursor)
            cursor.execute('SELECT * FROM "Usuarios" WHERE role_id = 2;')
            proveedor = dictfetchall(cursor)

           

        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()
        context = {'datos': user, 'producto' : product, 'conectTipo' : tipos,'conectProveedor' : proveedor}
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

def showmoreView(request):
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Productos";')
        product = dictfetchall(cursor)
    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
    finally:
        cursor.close()

    data = json.dumps(product)
    return HttpResponse(data, content_type='application/json')


def filtroProveedor(request, selectedProveedor):
    try:
        cursor = connection.cursor()
        if(selectedProveedor == 0):
            cursor.execute('SELECT * FROM "Productos";')
            queryType = dictfetchall(cursor)
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

    # si alguien que ya esta logueado intenta acceder a esta vista mediante la URL se le redirige a la pagina principal
    if request.user.is_authenticated:
        return redirect('home')
    
    # si la informacion que se manda por el formulario va en una peticion de tipo POST
    if request.method == "POST":
        email = request.POST.get('email') # se obtiene el valor del correo dado por el usuario
        pwd = request.POST.get("password") # se obtiene el valor de la contraseña dada por el usuario
        userFound = False # para saber si el correo esta dado de alta en la BBDD

        try: # Comprueba si el correo del usuario esta registrado en la base de datos
            user = User.objects.get(email=email)
            userFound = True
        except:
            messages.error(request, 'Este correo no esta registrado como usuario')

        if userFound: # si el correo esta dado de alta intenta hacer el login con la contraseña
            user = authenticate(request, username=email, password=pwd)

            if user is not None: # login correcto
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Contraseña incorrecta')

    return render(request, 'ecommerce/login.html')


def registrarse(request): # falta mucho curro por hacer aqui

    # si alguien que ya esta logueado intenta acceder a esta vista mediante la URL se le redirige a la pagina principal
    if request.user.is_authenticated:
        return redirect('home')
    
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            pwdConf = request.POST.get('password2')

            user = form.save(commit=False)

            if comprobarCampos(request, user, pwdConf):
                user.role_id = 2
                user.username = user.first_name
                user.save()
                login(request, user)
                return redirect('home')
            
        else:
            form_data = request.session.get('form_data', {})
            form = UserCreationForm(initial=form_data)

    return render(request, 'ecommerce/register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')