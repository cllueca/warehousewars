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
from django.views.decorators.csrf import csrf_exempt
    
from store.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def paginaPrincipal(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        columna = request.GET.get('columna')
        direction = request.GET.get('direction')
        query = request.GET.get("query")
        query_id = request.GET.get("query_id")
        query_stock_min = request.GET.get("query_stock_min")
        query_stock_max = request.GET.get("query_stock_max")
        query_min_stock_min = request.GET.get("query_min_stock_min")
        query_min_stock_max = request.GET.get("query_min_stock_max")
        query_price_min = request.GET.get("query_price_min")
        query_price_max = request.GET.get("query_price_max")
        
        if columna and direction:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "Productos" ORDER BY {columna} {direction}')
        else: 
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "Productos"')
        product = dictfetchall(cursor)

        if query:
            product = [p for p in product if query in p['name'] or query in p['location']]
        if query_id:
            product = [p for p in product if p['product_id'] == int(query_id)]
        
        if query_stock_min and query_stock_max:
            product = [p for p in product if p['stock'] >= int(query_stock_min) and p['stock'] <= int(query_stock_max)]

        if query_stock_min:
            product = [p for p in product if p['stock'] >= int(query_stock_min)]

        if query_stock_max:
            product = [p for p in product if p['stock'] <= int(query_stock_max)]    

        if query_min_stock_min and query_min_stock_max:
            product = [p for p in product if p['min_stock'] >= int(query_min_stock_min) and p['min_stock'] <= int(query_min_stock_max)]

        if query_min_stock_min:
            product = [p for p in product if p['min_stock'] >= int(query_min_stock_min)]

        if query_min_stock_max:
            product = [p for p in product if p['min_stock'] <= int(query_min_stock_max)]  

        if query_price_min and query_price_max:
            product = [p for p in product if float(p['cost_per_unit'].replace("$", "")) >= float(query_price_min) and float((p['cost_per_unit']).replace("$","")) <= float(query_price_max)]

        if query_price_min:
            product = [p for p in product if float(p['cost_per_unit'].replace("$","")) >= float(query_price_min)]

        if query_price_max:
            product = [p for p in product if float(p['cost_per_unit'].replace("$","")) <= float(query_price_max)]  

        context = {'producto' : product}
        return render(request, 'ecommerce/vistaAlmacen.html', context)
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
        context = {'datos': user, 'producto' : product, 'productoCarrousel' : productCarrousel, 'conectTipo' : tipos,'conectProveedor' : proveedor}
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

def pagincaCarrito(request):

    return render(request, 'ecommerce/carrito.html')


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

@csrf_exempt
def update_product(request, product_id):

    if request.method == "POST":
        product_id = request.POST.get('productId')
        name = request.POST.get('name')
        stock = int(request.POST.get('stock'))
        min_stock = int(request.POST.get('min_stock'))
        cost_per_unit = float(request.POST.get('cost_per_unit'))
        location = request.POST.get('location')
        image_url = request.POST.get('image_url')
        product_description = request.POST.get('product_description')
        type_id = int(request.POST.get('type_id'))
        fecha_llegada = datetime.datetime.strptime(request.POST.get('fecha_llegada'), '%Y-%m-%d').date()
        print(fecha_llegada)
        try:
            cursor = connection.cursor()
          
            query = 'UPDATE "Productos" SET name = %s, stock = %s, min_stock = %s, cost_per_unit = %s, location = %s, image_url = %s, product_description = %s, type_id = %s, fecha_llegada = %s WHERE product_id = %s'
            values = [name, stock, min_stock, cost_per_unit, location, image_url, product_description, type_id, fecha_llegada, product_id]
            #print(cursor.mogrify(query, values))
            #print("Types: ", [type(v) for v in values])
            cursor.execute(query, values)
       
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()
    
        return JsonResponse({"message": "Producto actualizado"})
    return HttpResponse("Metodo no permitido")


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        stock = int(request.POST.get('stock'))
        min_stock = int(request.POST.get('min_stock'))
        cost_per_unit = float(request.POST.get('cost_per_unit'))
        location = request.POST.get('location')
        image_url = request.POST.get('image_url')
        product_description = request.POST.get('product_description')
        type_id = int(request.POST.get('type_id'))
        fecha_llegada = datetime.datetime.strptime(request.POST.get('fecha_llegada'), '%Y-%m-%d').date()
        print(fecha_llegada)
        try:
            cursor = connection.cursor()
            
            query = 'INSERT INTO "Productos" (name, stock, min_stock, cost_per_unit, location, image_url, product_description, type_id, fecha_llegada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = [name, stock, min_stock, cost_per_unit, location, image_url, product_description, type_id, fecha_llegada]
            print(cursor.mogrify(query, values))
            cursor.execute(query, values)
    
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()

        return JsonResponse({"message": "Producto creado"})
    return HttpResponse("Metodo no permitido")


def delete_product(request, product_id):
    if request.method == "POST":
        product_id = request.POST.get('productId')
        print(product_id)
        try:
            cursor = connection.cursor()
            
            query = 'DELETE FROM "Productos" WHERE product_id = %s'
            values = [product_id]
            cursor.execute(query, values)
    
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()

        return JsonResponse({"message": "Producto eliminado"})
    return HttpResponse("Metodo no permitido")

# Funciones Carrito

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')