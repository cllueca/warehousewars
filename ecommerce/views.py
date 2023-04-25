from django.utils import timezone
from django.shortcuts import render, redirect
from django.db import connection, transaction
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from ecommerce.models import User, Albaranes, Pedidos, Estados, Tipos
from .funciones import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Estados, PedidoProductos, Pedidos, Productos, Transportistas, Usuarios

from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import FileResponse
from django.http import Http404

from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import F, Prefetch, Subquery, OuterRef
from django.core.mail import EmailMessage

from datetime import datetime, timedelta


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
        cursor.execute(f'SELECT p.*, s.name as status_name, s.status_id as status_status_id FROM "Pedidos" p JOIN "Estados" s ON p.status_id = s.status_id ORDER BY {columnaPedido} {directionPedido}')
        order = dictfetchall(cursor)
    else:
        cursor = connection.cursor()
        cursor.execute(f'SELECT p.*, s.name as status_name, s.status_id as status_status_id FROM "Pedidos" p JOIN "Estados" s ON p.status_id = s.status_id')
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
        product = [p for p in product if p['price'] >= float(query_product_price_min) and (p['price']) <= float(query_product_price_max)]

    if query_product_price_min:
        product = [p for p in product if p['price'] >= float(query_product_price_min)]

    if query_product_price_max:
        product = [p for p in product if p['price'].replace("$","") <= float(query_product_price_max)]  

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
    estados = Estados.objects.all()
    context = {'producto' : product, 'usuario' : user, 'pedido' : order, 'pedidoProv' : orderProv, 'estados': estados}
    return context


def paginaPrincipal(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        context = vistaAlmacen(request)
        return render(request, 'ecommerce/vistaAlmacen.html', context)
    else:
        try:
            user = User.objects.all()
            product = Productos.objects.all()[:6]
            productCarrousel = Productos.objects.all()[:5]
            tipos = Tipos.objects.all()
            proveedor = User.objects.filter(role_id=2)
            print(proveedor)
        except Exception as e:
            print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))

        context = {'datos': user, 'producto': product, 'productoCarrousel': productCarrousel, 'conectTipo': tipos, 'conectProveedor': proveedor}
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


def pagincaCarrito(request):

    return render(request, 'ecommerce/carrito.html')


def filtroInicio(request, selectedValue):
    queryType = []
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

@api_view(['GET'])
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
    if selectedProveedor == 0:
        productos = Productos.objects.all().values()
    else:
        productos = Productos.objects.filter(id=selectedProveedor).values()

    productos_list = list(productos)
    return JsonResponse(productos_list, safe=False)



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
            messages.error(request, 'Este correo no se encuentra en la base de datos')
            

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
                                              request.POST.get('adress')
                                              )
        
        correcto = comprobarContraseña(request, request.POST.get('password'), request.POST.get('password2')) if correcto else False

        if(correcto):
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                first_name=request.POST.get('username'),
                last_name=request.POST.get('apellidos'),
                adress=request.POST.get('adress'),
                email=request.POST.get('correo'),
                telefono=request.POST.get('telefono'),
                role_id=2,
            )

            user.save()
            login(request, user)
            is_authenticated = request.user.is_authenticated
            context = {'is_authenticated': is_authenticated}
            return render(request,"ecommerce/inicio.html", context)


    return render(request, 'ecommerce/register.html')



def logoutUser(request):
    logout(request)
    return redirect('home')

def cambiarPwd(request):

    if request.method == "POST":
        userFound = False

        try: # Comprueba si el correo del usuario esta registrado en la base de datos
                usuario = User.objects.get(email=request.POST.get('email'))
                userFound = True
        except:
            messages.error(request, 'Este correo no se encuentra en la base de datos')
        
        if userFound:
            
            if comprobarContraseña(request, request.POST.get('password'), request.POST.get('password2')):
                usuario.set_password(request.POST.get('password'))
                usuario.save()
                messages.success(request, "Contraseña cambiada")
                return redirect('login')
        
    return render(request, 'ecommerce/cambiarPwd.html')

@login_required(login_url='login')
def perfilUsuario(request):
    idUser = request.user.id

    try:
        pedidos = Pedidos.objects.filter(user_id=idUser).prefetch_related(
            Prefetch('pedidoproductos_set', queryset=PedidoProductos.objects.select_related('product_id'))
        )

        fechasEntrega = {}
        for pedido in pedidos:
            if pedido.transportista.name == "SEUR":
                if pedido.isUrgent:
                    fechasEntrega[pedido.pedido_id] = pedido.date_order + timedelta(days=1)
                else:
                    fechasEntrega[pedido.pedido_id] = pedido.date_order + timedelta(days=3)
    except Exception as e:
        print("Ha ocurrido un error en la consulta a la BBDD {}".format(e))

    return render(request, 'ecommerce/perfil.html', {"pedidos": pedidos, "fechasEntrega": fechasEntrega})


@csrf_exempt
def update_product(request, product_id):

    if request.method == "POST":
        product_id = int(request.POST.get('product_id'))
        name = request.POST.get('product_name')
        stock = int(request.POST.get('product_stock'))
        min_stock = int(request.POST.get('product_min_stock'))
        cost_per_unit = float(request.POST.get('product_cost'))
        location = request.POST.get('product_location')
        type_id = int(request.POST.get('product_type_id'))
        fecha_llegada = datetime.datetime.strptime(request.POST.get('product_fecha'), '%Y-%m-%d').date()
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
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.adress = request.POST.get('direccion')
        user.email = request.POST.get('correo')
        user.telefono = request.POST.get('telefono')
        user.role_id = int(request.POST.get('roleId'))
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

@login_required(login_url="login")
def mandarPedido(request,tipo_envio, transportista ):
    # Get the user's cart
    cart = Cart(request)
    today = timezone.now().astimezone(timezone.get_current_timezone()).date()
    estado = Estados.objects.get(pk=5)  # Get the Estados instance with a primary key of 5
    transportista = Transportistas.objects.get(pk=transportista)
    idUser = request.user.id
    user = User.objects.get(pk=idUser)
    # Create a new Pedido instance
    total = 0
    total_weight = 0

    if(tipo_envio):
        total = 5.75
    else:
        total = 0

    for item in cart.cart:
        product_id = item
        quantity = cart.cart.get(str(product_id), {}).get('quantity', 0)
        price = cart.cart.get(str(product_id), {}).get('price', 0)
        product = Productos.objects.get(pk=product_id)
        weight = product.weight
        total = total + (float(price) * float(quantity))
        total_weight = total_weight  + (float(weight) * float(quantity))

    pedido = Pedidos(date_order=today, status =estado, total_cost=total, user=user, address=user.adress , total_weight=total_weight  , isUrgent=tipo_envio , transportista= transportista)
    # Save the Pedido instance to the database
    if len(cart.cart) != 0:
        pedido.save()
        idPedido = pedido.pedido_id
        # Create a PedidoProducto instance for each item in the cart
        for item in cart.cart:
            product_id = item
            quantity = cart.cart.get(str(product_id), {}).get('quantity', 0)
            price = cart.cart.get(str(product_id), {}).get('price', 0)
            total = (float(price) * float(quantity))
            producto = Productos.objects.get(pk=product_id)
            pedidoproductos = PedidoProductos(product_id = producto, pedido_id = pedido   , quantity = quantity, total_cost = total)
            pedidoproductos.save()

            # Update the Producto stock
            producto = Productos.objects.get(pk=product_id)
            producto.stock -= quantity
            producto.save()

        # Clear the user's cart
        cart.clear()

            # Send email
        email_subject = "Pedido recibido"
        email_body = "Hola {},\n\nTu pedido con ID {} ha sido recibido. Estamos procesando tu pedido y te notificaremos cuando esté listo para ser enviado.\n\nGracias por comprar con nosotros.".format(user.username, idPedido)
        email = EmailMessage(
            email_subject,
            email_body,
            "d38df7490e64e7@inbox.mailtrap.com",  # Cambia esto por la dirección de correo electrónico de tu tienda
            [user.email],
        )

        try:
            email.send()
        except Exception as e:
            print("Error al enviar el correo electrónico:", e)

        # Redirect to a success page
        is_authenticated = request.user.is_authenticated
        context = {'is_pedido': True}
        return render(request, "ecommerce/inicio.html", context)
    else:
        return redirect("carrito")


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")

@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.remove(product)
    return redirect("/carrito")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.add(product=product)
    return redirect("/carrito")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Productos.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/carrito")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/carrito")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, '/carrito')



def generate_albaran_pdf(request, pedido_id):
    albaran = Albaranes.objects.get(pedido_id=pedido_id)
    template = get_template('ecommerce/albaranPedido.html')
    context = {'albaran': albaran}
    html = template.render(context)
    buffer = BytesIO()
    pisa.CreatePDF(html, dest=buffer)

    buffer.seek(0)
    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="albaran{pedido_id}.pdf"'
    return response

@csrf_exempt
def delete_order(request, order_id):
    if request.method == "POST":
        try:
            order = Pedidos.objects.get(pedido_id=order_id)
            print(f"Pedido encontrado: {order.pedido_id}")

            PedidoProductos.objects.filter(pedido_id=order).delete()
            print("Productos del pedido eliminados")

            order.delete()
            print("Pedido eliminado")

            return JsonResponse({"status": "success"}, status=200)
        except Pedidos.DoesNotExist:
            print(f"Pedido no encontrado: {order_id}")
            return JsonResponse({"status": "error"}, status=404)
    else:
        print("Solicitud no válida")
        return JsonResponse({"status": "error"}, status=400)

def success_page(request):
    return render(request, 'ecommerce/inicio.html')



def paginaContacto(request):
    idUser = request.user.id
    user = User.objects.get(pk=idUser)
    if request.method == 'POST':
        sender_email = request.POST['email']
        message = request.POST['message']

        email = EmailMessage(
            'Incidencias web SlotsSolutions',
            "Mesaje enviado por: <{}>: \n\n {}".format(sender_email, message),
            from_email=user.email,  # Reemplaza esto con la dirección de correo electrónico de tu tienda
            to=['d38df7490e64e7@inbox.mailtrap.com'],  # Asegúrate de utilizar tu correo personalizado aquí
        )
        try:
            email.send()
            return HttpResponseRedirect(reverse('contacto') + '?ok')
        except Exception as e:
            print("Error al enviar el correo electrónico:", e)
            return HttpResponseRedirect(reverse('contacto') + '?error')
    else:
        return render(request, 'ecommerce/contacto.html')  # Cambia 'contact.html' por la plantilla de la página de contacto

@csrf_exempt
def update_order_status(request, order_id, status_id):
    if request.method == "POST":
        try:
            order = Pedidos.objects.get(pedido_id=order_id)
            new_status = Estados.objects.get(status_id=status_id)
            # Asegúrate de convertir el valor de `total_cost` en un float antes de guardarlo
            order.total_cost = float(order.total_cost.replace('$', ''))
            order.status = new_status
            order.save()
            return JsonResponse({"status": "success"}, status=200)
        except (Pedidos.DoesNotExist, Estados.DoesNotExist, ValueError):
            return JsonResponse({"status": "error"}, status=404)
    else:
        return JsonResponse({"status": "error"}, status=400)
