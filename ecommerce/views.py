from django.utils import timezone
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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Estados, PedidoProductos, Pedidos, Productos, Usuarios


def vistaAlmacen(request):
    columnaProduct = request.GET.get('columna')
    directionProduct = request.GET.get('direction')
    query_product_name = request.GET.get("query_product_name")
    query_product_locate = request.GET.get("query_product_locate")
    query_product_id = request.GET.get("query_product_id")
    query_product_stock_min = request.GET.get("query_product_stock_min")
    query_product_stock_max = request.GET.get("query_product_stock_max")
    query_product_min_stock_min = request.GET.get("query_product_min_stock_min")
    query_product_min_stock_max = request.GET.get("query_product_min_stock_max")
    query_product_price_min = request.GET.get("query_product_price_min")
    query_product_price_max = request.GET.get("query_product_price_max")

    columnaUser = request.GET.get('columnaUser')
    directionUser = request.GET.get('directionUser')
    query_id_user = request.GET.get('query_id_user')
    query_nombre_user = request.GET.get('query_nombre_user')
    query_apellido_user = request.GET.get('query_apellido_user')
    query_correo_user = request.GET.get('query_correo_user')
    query_direccion_user = request.GET.get('query_direccion_user')
    query_telefono_user = request.GET.get('query_telefono_user')
    query_roleId_user = request.GET.get('query_roleId_user')

    columnaPedido = request.GET.get('columnaPedido ')
    directionPedido  = request.GET.get('directionPedido ')
    query_pedido_id = request.GET.get('query_pedido_id')
    query_pedido_statusId = request.GET.get('query_pedido_statusId')
    query_pedido_price_min = request.GET.get('query_pedido_price_min')
    query_pedido_price_max = request.GET.get('query_pedido_price_max')
    query_pedido_userId = request.GET.get('query_pedido_userId')
    query_pedido_address = request.GET.get('query_pedido_address')

    columnaPedidoProv = request.GET.get('columnaPedidoProv')
    directionPedidoProv  = request.GET.get('directionPedidoProv')
    query_orderProv_provProdId = request.GET.get('query_orderProv_provProdId')
    query_orderProv_userId = request.GET.get('query_orderProv_userId')
    query_orderProv_productId = request.GET.get('query_orderProv_productId')

    
    if columnaProduct and directionProduct:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Productos" ORDER BY {columnaProduct} {directionProduct}')
        product = dictfetchall(cursor)
    else:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Productos"')
        product = dictfetchall(cursor)

    if columnaUser and directionUser:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "ecommerce_user" ORDER BY {columnaUser} {directionUser}')
        user = dictfetchall(cursor)
    else:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "ecommerce_user"')
        user = dictfetchall(cursor)

    if columnaPedido and directionPedido:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Pedidos" ORDER BY {columnaPedido} {directionPedido}')
        order = dictfetchall(cursor)
    else:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Pedidos"')
        order = dictfetchall(cursor)
    
    if columnaPedidoProv and directionPedidoProv:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Proveedor-Producto" ORDER BY {columnaPedidoProv} {directionPedidoProv}')
        orderProv = dictfetchall(cursor)
    else:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM "Proveedor-Producto"')
        orderProv = dictfetchall(cursor)

    if query_product_name: #chars
        product = [p for p in product if query_product_name in p['name']]
    if query_product_locate: #chars
        product = [p for p in product if query_product_locate in p['location']]
            
    if query_product_id: #Int
        product = [p for p in product if p['id'] == int(query_product_id)]
    
    if query_product_stock_min and query_product_stock_max:
        product = [p for p in product if p['stock'] >= int(query_product_stock_min) and p['stock'] <= int(query_product_stock_max)]

    if query_product_stock_min:
        product = [p for p in product if p['stock'] >= int(query_product_stock_min)]

    if query_product_stock_max:
        product = [p for p in product if p['stock'] <= int(query_product_stock_max)]    

    if query_product_min_stock_min and query_product_min_stock_max:
        product = [p for p in product if p['min_stock'] >= int(query_product_min_stock_min) and p['min_stock'] <= int(query_product_min_stock_max)]

    if query_product_min_stock_min:
        product = [p for p in product if p['min_stock'] >= int(query_product_min_stock_min)]

    if query_product_min_stock_max:
        product = [p for p in product if p['min_stock'] <= int(query_product_min_stock_max)]  

    if query_product_price_min and query_product_price_max:
        product = [p for p in product if float(p['price'].replace("$", "")) >= float(query_product_price_min) and float((p['price']).replace("$","")) <= float(query_product_price_max)]

    if query_product_price_min:
        product = [p for p in product if float(p['price'].replace("$","")) >= float(query_product_price_min)]

    if query_product_price_max:
        product = [p for p in product if float(p['price'].replace("$","")) <= float(query_product_price_max)]  

    if query_nombre_user: #chars
        user = [p for p in user if query_nombre_user in p['first_name']]

    if query_apellido_user: #chars
        user = [p for p in user if query_apellido_user in p['last_name']]

    if query_correo_user: #chars
        user = [p for p in user if query_correo_user in p['email']]
    
    if query_direccion_user: #chars
        user = [p for p in user if query_direccion_user in p['adress']]

    if query_telefono_user: #chars
        user = [p for p in user if query_telefono_user in p['telefono']]

    if query_roleId_user: #chars
        user = [p for p in user if p['role_id'] == int(query_roleId_user)]

    if query_id_user: #chars
        user = [p for p in user if p['id'] == int(query_id_user)]

    if query_pedido_id: #chars
        order = [p for p in order if p['pedido_id'] == int(query_pedido_id)]
    
    if query_pedido_statusId: #chars
        order = [p for p in order if p['status_id'] == int(query_pedido_statusId)]

    if query_pedido_userId: #chars
        order = [p for p in order if p['user_id'] == int(query_pedido_userId)]
   
    if query_pedido_address: #chars
        order = [p for p in order if query_pedido_address in p['address']]
    
    if query_pedido_price_min and query_pedido_price_max:
        order = [p for p in order if float(p['total_cost'].replace("$", "")) >= float(query_pedido_price_min) and float((p['total_cost']).replace("$","")) <= float(query_pedido_price_max)]

    if query_pedido_price_min:
        order = [p for p in order if float(p['total_cost'].replace("$","")) >= float(query_pedido_price_min)]

    if query_pedido_price_max:
        order = [p for p in order if float(p['total_cost'].replace("$","")) <= float(query_pedido_price_max)]  
    
    if query_orderProv_userId: #chars
        orderProv = [p for p in orderProv if p['user_id'] == int(query_orderProv_userId)]
    
    if query_orderProv_provProdId: #chars
        orderProv = [p for p in orderProv if p['provprod_id'] == int(query_orderProv_provProdId)]
    
    if query_orderProv_productId: #chars
        orderProv = [p for p in orderProv if p['product_id'] == int(query_orderProv_productId)]
     
    context = {'producto' : product, 'usuario' : user, 'pedido' : order, 'pedidoProv' : orderProv}
    return context


def paginaPrincipal(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        context = vistaAlmacen(request)
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
        cursor.execute('SELECT * FROM "Productos" WHERE id = %s ',[productId])
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
            cursor.execute('SELECT * FROM "Productos" ORDER BY price ASC;')
        else:
            cursor.execute('SELECT * FROM "Productos" ORDER BY price DESC;')
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
            cursor.execute('SELECT * FROM "Proveedor-Producto" JOIN "Usuarios" ON "Usuarios".user_id = "Proveedor-Producto".user_id JOIN "Productos" ON "Productos".id = "Proveedor-Producto".id WHERE "Usuarios".user_id = %s', [selectedProveedor])        
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


def registrarse(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        correcto = camposObligatoriosRellenos(request,
                                              request.POST.get('username'),
                                              request.POST.get('apellidos'),
                                              request.POST.get('telefono'),
                                              request.POST.get('correo'),
                                              request.POST.get('password'),
                                              request.POST.get('password2'))
        
        correcto = comprobarContraseña(request, request.POST.get('password'), request.POST.get('password2')) if correcto else None

        if(correcto): # funcion un poco basica, mejorar mas adelante
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
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

@csrf_exempt
def update_product(request, id):

    if request.method == "POST":
        product_id = request.POST.get('productId')
        name = request.POST.get('NEWproductName')
        stock = int(request.POST.get('NEWproductStock'))
        min_stock = int(request.POST.get('NEWproductMinStock'))
        cost_per_unit = float(request.POST.get('NEWproductCost'))
        location = request.POST.get('NEWproductLocation')
        type_id = int(request.POST.get('type_id'))
        fecha_llegada = datetime.datetime.strptime(request.POST.get('fecha_llegada'), '%Y-%m-%d').date()
        print(fecha_llegada)
        try:
            cursor = connection.cursor()
          
            query = 'UPDATE "Productos" SET name = %s, stock = %s, min_stock = %s, price = %s, location = %s, type_id = %s, fecha_llegada = %s WHERE id = %s'
            values = [name, stock, min_stock, cost_per_unit, location, type_id, fecha_llegada, product_id]
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
        cost_per_unit = float(request.POST.get('price'))
        location = request.POST.get('location')
        image_url = request.POST.get('image_url')
        product_description = request.POST.get('product_description')
        type_id = int(request.POST.get('type_id'))
        fecha_llegada = datetime.datetime.strptime(request.POST.get('fecha_llegada'), '%Y-%m-%d').date()
        print(fecha_llegada)
        try:
            cursor = connection.cursor()
            
            query = 'INSERT INTO "Productos" (name, stock, min_stock, price, location, image_url, product_description, type_id, fecha_llegada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = [name, stock, min_stock, cost_per_unit, location, image_url, product_description, type_id, fecha_llegada]
            print(cursor.mogrify(query, values))
            cursor.execute(query, values)
    
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()

        return JsonResponse({"message": "Producto creado"})
    return HttpResponse("Metodo no permitido")

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        user = User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password'),
                    first_name=request.POST.get('nombre'),
                    last_name=request.POST.get('apellidos'),
                    #direccion=request.POST.get('direccion'),
                    email=request.POST.get('correo'),
                    telefono=request.POST.get('telefono'),
                    role_id=int(request.POST.get('role_id')),
                )
        user.save()
    return HttpResponse("Metodo no permitido")

@csrf_exempt
def edit_user(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.email = request.POST.get('correo')
        user.telefono = request.POST.get('telefono')
        user.role_id = int(request.POST.get('role_id'))
        user.save()
        return HttpResponse("Usuario actualizado exitosamente")
    return HttpResponse("Método no permitido")

def delete_product(request, id):
    if request.method == "POST":
        id = request.POST.get('productId')
        print(id)
        try:
            cursor = connection.cursor()
            
            query = 'DELETE FROM "Productos" WHERE id = %s'
            values = [id]
            cursor.execute(query, values)
    
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()

        return JsonResponse({"message": "Producto eliminado"})
    return HttpResponse("Metodo no permitido")



def delete_user(request, user_id):
    if request.method == "POST":
        print(user_id)
        try:
            cursor = connection.cursor()
            
            query = 'DELETE FROM "ecommerce_user" WHERE id = %s'
            values = [user_id]
            cursor.execute(query, values)
    
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))
        finally:
            cursor.close()

        return JsonResponse({"message": "Usuario eliminado"})
    return HttpResponse("Metodo no permitido")
# Funciones Carrito

@login_required(login_url="/users/login")
def mandarPedido(request):
    # Get the user's cart
    cart = Cart(request)
    today = timezone.now().astimezone(timezone.get_current_timezone()).date()
    estado = Estados.objects.get(pk=5)  # Get the Estados instance with a primary key of 5
    idUser = request.user.id
    user = User.objects.get(pk=idUser)
    # Create a new Pedido instance
    pedido = Pedidos(date_order=today, status=estado, total_cost=12, user=user, address='ejemplo5')
    # Save the Pedido instance to the database
    pedido.save()
    idPedido = pedido.pedido_id
    # Create a PedidoProducto instance for each item in the cart
    for item in cart.cart:
        product_id = item
        quantity = cart.cart.get(str(product_id), {}).get('quantity', 0)
        pedidoproductos = PedidoProductos(product_id = product_id,pedido_id = idPedido,quantity = quantity,total_cost = 12)
        pedidoproductos.save()

    # Clear the user's cart
    cart.clear()
    # Redirect to a success page
    return redirect("home")


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.remove(product)
    return redirect("/carrito")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.add(product=product)
    return redirect("/carrito")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/carrito")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/carrito")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, '/carrito')

