/*$(document).ready(function() {
  $("#product-type").change(function(){
    var selectedValue = $(this).val();
    $.ajax({
        url: '',
        success: function(response){
            $("#here").html(response);
            console.log("valor: " + response)
        }
    });
  });
});*/

document.addEventListener("DOMContentLoaded", function() {
  let selected = false;
  let selectedValue, selectedPrize, selectedProveedor;
  const contenedor = document.getElementById("here");

  $("#product-type").change(function() {
    selectedValue = this.value;
    if (selectedValue != "0") {
      selected = true;
      url = `/filtroInicio/${selectedValue}/`
      $("#product-prize, #product-proveedor").val("0").change();
      updateProducts(url);
    }
  });

  $("#product-prize").change(function() {
    selectedPrize = this.value;
    if (selectedPrize != "0") {
      selected = true;
      url = `/filtroPrecio/${selectedPrize}/`
      $("#product-type, #product-proveedor").val("0").change();
      updateProducts(url);
    }
  });

  $("#product-proveedor").change(function() {
    selectedProveedor = this.value;
    if (selectedProveedor != "0") {
      selected = true;
      url = `/filtroProveedor/${selectedProveedor}/`
      $("#product-type, #product-prize").val("0").change();
      updateProducts(url);
    }
  });

  function updateProducts() {
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Status code error: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        while (contenedor.firstChild) {
          contenedor.removeChild(contenedor.firstChild);
        }
        contenedor.innerHTML = "";
        let productos = data;
        for (let i = 0; i < productos.length; i++) {
          contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info" id="product-${productos[i].id}" data-product-id="${productos[i].id}">
            <div class="card">
              <img src="${productos[i].image}" class="imageCard card-img-top mx-auto d-block" alt="#">
              <hr style="border-color: #FEA424;">
              <div class="card-body d-flex justify-content-between">
                <div>
                  <h5 class="card-title">${productos[i].name}</h5>
                </div>
                <div class="text-right">
                  <p class="card-text borderPrize">${productos[i].price} €</p>
                </div>
              </div>
            </div>
            </div>`;
        }
      });
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const select = document.getElementById("product-prize");
  select.addEventListener("mouseenter", function() {
  this.size = this.options.length + 2.2;
  select.style.transform = "scale(1.1)";
  this.style.color = "black";
  });
  select.addEventListener("mouseleave", function() {
  this.size = 1;
  select.style.transform = "scale(1)";
  select.style.overflow = "hidden";
  this.style.color = "black";
  });
  
  const option0 = document.getElementById("option-0");
  option0.addEventListener("mouseenter", function() {
  this.style.backgroundColor = "#062995";
  this.style.color = "#fff";
  });
  option0.addEventListener("mouseleave", function() {
  this.style.backgroundColor = "";
  this.style.color = "black";
  });
  
  const option1 = document.getElementById("option-1");
  option1.addEventListener("mouseenter", function() {
  this.style.backgroundColor = "#062995";
  this.style.color = "#fff";
  
  });
  option1.addEventListener("mouseleave", function() {
  this.style.backgroundColor = "";
  this.style.color = "black";
  });
  
  const option2 = document.getElementById("option-2");
  option2.addEventListener("mouseenter", function() {
  this.style.backgroundColor = "#062995";
  this.style.color = "#fff";
  });
  option2.addEventListener("mouseleave", function() {
  this.style.backgroundColor = "";
  this.style.color = "black";
  });
  });


$(document).ready(function() {
  $(document).on("click", ".product-info", function() {
    var $element = $(this);
    var productId = $element.data('product-id');
    console.log("Valor id: " + productId)
    location.href = '/descProducto/' + productId + '/'; 
  });
});
 //location.href = '/descProducto/' + productId + '/';    onclick="location.href='/descProducto/' + this.dataset.productId + '/'"


 $(document).ready(function() {
  $('#minus').click(function() {
let units = document.getElementById("units");
  if (units.value > 1) {
    units.value--;
  }
  });
});

$(document).ready(function() {
  $('#plus').click(function() {
    let units = document.getElementById("units");
    units.value++;
  });

});


 //location.href = '/descProducto/' + productId + '/';    onclick="location.href='/descProducto/' + this.dataset.productId + '/'"


 $(document).ready(function() {
  console.log("SS")
  var button = $('#show-more');
  console.log(button);
  button.click(function() {

    fetch("http://127.0.0.1:8000/showmore/")
    .then(response => response.json())
    .then(data => {
        //aqui recibiras el json y puedes mostrarlo en tu vista

        let productos = data;
        let contenedor = document.getElementById("here")
        while (contenedor.firstChild) {
          contenedor.removeChild(contenedor.firstChild);
        }
        contenedor.innerHTML = "";
        console.log(contenedor);
        for (let i = 0; i < productos.length; i++) {
          contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info" id="product-${productos[i].id}" data-product-id="${productos[i].id}">
          <div class="card" >
          
            <img src="${productos[i].image}" class="imageCard card-img-top mx-auto d-block"  alt="#" >

            <hr style="border-color: #FEA424;">
            <div class="card-body d-flex justify-content-between">
              <div>
                <h5 class="card-title">${productos[i].name}</h5>
              </div>
              <div class="text-right">
                <p class="card-text borderPrize">${productos[i].price} €</p>
              </div>
            </div>
          </div>
          </div>`;
        }
        contenedor.innerHTML += `<div class="text-center mt-4" style="width: 100%;">
        <button id="show-less-button" class="button-38" role="button">Ver Menos</button>
        </div>`;
        // Agregar el evento click para el botón "Ver Menos"
        $('#show-less-button').on('click', function() {
          window.location.reload()
        });
    });
  });
 
});

$(document).ready(function () {
  $('.btn-warning').click(function () {
    var productId = $(this).data('product-id');
    $('#productId').val(productId);

  });
});

function updateProduct() {
  const productId = $('#productId').val();

  const formData = new FormData(document.getElementById("editProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);

  const url = `/update/${productId}/`;

  fetch(url, {
    method: "POST",
    body: formData
  })
}

$(document).ready(function () {
  $("#createProductForm").on("submit", function(e) {
    e.preventDefault();
    createProduct();
  });
});

function createProduct() {

  const formData = new FormData(document.getElementById("createProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  
  const url = `/create/`;
  
  fetch(url, {
    method: "POST",
    body: formData,
   
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {


      // handle response data
      alert(data.message);
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal

    $("#editProductModal").modal("hide");

    // Limpia los parámetros
    $("#editProductForm")[0].reset();
};

$(document).ready(function () {
  $("#createProductForm").on("submit", function(e) {
    e.preventDefault();
    createProduct();
  });
});

// $(document).on("click", "#botonEditProductos", function (event) {
//   var boton = document.getElementById('botonEditProductos');
//   var cosas = boton.dataset;
//   // for (var i = 0; i < cosas.length; i++){
//   //   console.log(i + " ---> " + cosas[i]);
//   // }
//   var modalNombre = document.getElementById('NEWproductName');
//   var modalStock = document.getElementById('NEWproductStock');
//   var modalMinStock = document.getElementById('NEWproductMinStock');
//   var modalCost = document.getElementById('NEWproductCost');
//   var modalLocation = document.getElementById('NEWproductLocation');
//   var modalTypeId = document.getElementById('NEWproductTypeid');
//   var modalFecha = document.getElementById('NEWproductFecha');
//   modalNombre.value = cosas[0];
//   modalStock.value = int(cosas[1]);
//   modalMinStock.value = int(cosas[2]);
//   modalCost.value = float(cosas[3]);
//   modalLocation.value = cosas[4];
//   modalTypeId.value = cosas[5];
//   modalFecha.value = cosas[6];
// });

function createProduct() {

  const formData = new FormData(document.getElementById("createProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  
  const url = `/create/`;

    $("#createProductModal").modal("hide");

    // Limpia los parámetros
    $("#createProductForm")[0].reset();
    
    // Recarga la página
    location.reload();
};

function createUser() {

  const formData = new FormData(document.getElementById("createUserForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  
  const url = `/createUser/`;
  
  fetch(url, {
    method: "POST",
    body: formData,
   
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      alert(data.message);
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal

    $("#createProductModal").modal("hide");

    // Limpia los parámetros
    $("#createProductForm")[0].reset();

    $("#createUserModal").modal("hide");

    // Limpia los parámetros
    $("#createUserForm")[0].reset();

    
    // Recarga la página
    location.reload();
};

$(document).ready(function () {
  $('.btn-danger').click(function () {
  var productId = $(this).data('product-id');
  $('#productId').val(productId);
  var userId = $(this).data('user-id');
  $('#userId').val(userId);
  }
)});

$(document).ready(function () {
    $('.btn-warning').click(function () {

    var modalID = document.getElementById('NEWproductId')
    var modalNombre = document.getElementById('NEWproductName');
    var modalStock = document.getElementById('NEWproductStock');
    var modalMinStock = document.getElementById('NEWproductMinStock');
    var modalCost = document.getElementById('NEWproductCost');
    var modalLocation = document.getElementById('NEWproductLocation');
    var modalTypeId = document.getElementById('NEWproductTypeid');
    var modalFecha = document.getElementById('NEWproductFecha');
      
    var productId = $(this).data('product-id');
    modalID.value = productId;
    var productName = $(this).data('product-name');
    modalNombre.value = productName;
    var productStock = $(this).data('product-stock');
    modalStock.value = productStock;
    var productMinStock = $(this).data('product-stockmin');
    modalMinStock.value = productMinStock;
    var productCost= $(this).data('product-cost');
    modalCost.value = productCost;
    var productLocation= $(this).data('product-location');
    modalLocation.value = productLocation;
    var productTypeid = $(this).data('product-typeid');
    modalTypeId.value = productTypeid;
    var productFecha = $(this).data('product-fecha');
    modalFecha.value = productFecha;



    var modaleUserId = document.getElementById('NEWuserId');
    var modalUsername = document.getElementById('NEWusername');
    var modalUserNombre = document.getElementById('NEWnombre');
    var modalUserApe = document.getElementById('NEWapellidos');
    var modalUserDir = document.getElementById('NEWdireccion');
    var modalUserCorreo = document.getElementById('NEWcorreo');
    var modalUserTelefono = document.getElementById('NEWtelefono');
    var modalUserRole = document.getElementById('NEWrole_id');

    var userId = $(this).data('user-id');
    modaleUserId.value = userId;
    var username = $(this).data('username');
    modalUsername.value = username;
    var nombre = $(this).data('nombre');
    modalUserNombre.value = nombre;
    var apellidos = $(this).data('apellidos');
    modalUserApe.value = apellidos;
    var direccion = $(this).data('direccion');
    modalUserDir.value = direccion;
    var correo = $(this).data('correo');
    modalUserCorreo.value = correo;
    var telefono = $(this).data('telefono');
    modalUserTelefono.value = telefono;
    var roleId = $(this).data('role-id');
    modalUserRole.value = roleId;
    
  });
});


function updateProduct() {
  const productId = $('#productId').val();
 
  const productName = $('#productName').val();
  const productStock = $('#productStock').val();
  const productMinStock = $('#productMinStock').val();
  const productCost = $('#productCost').val();
  const productLocation = $('#productLocation').val();
  const productTypeid = $('#productTypeid').val();
  const productFecha = $('#productFecha').val();

  const NEWproductId = $('#NEWproductId').val();
  const NEWproductName = $('#NEWproductName').val();
  const NEWproductStock = $('#NEWproductStock').val();
  const NEWproductMinStock = $('#NEWproductMinStock').val();
  const NEWproductCost = $('#NEWproductCost').val();
  const NEWproductLocation = $('#NEWproductLocation').val();
  const NEWproductTypeid = $('#NEWproductTypeid').val();
  const NEWproductFecha = $('#NEWproductFecha').val();

  const formData = new FormData(document.getElementById("editProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);

  if (NEWproductId) {
    formData.append("product_id", NEWproductId); // If there's a value in NEWproductId, update the corresponding column
  } else {
    formData.append("product_id", productId); // If NEWproductId is empty, keep the previous value
  }

  if (NEWproductName) {
    formData.append("product_name", NEWproductName); // If there's a value in NEWproductName, update the corresponding column
  } else {
    formData.append("product_name", productName); // If NEWproductName is empty, keep the previous value
  }

  if (NEWproductStock) {
    formData.append("product_stock", NEWproductStock); // If there's a value in NEWproductStock, update the corresponding column
  } else {
    formData.append("product_stock", productStock); // If NEWproductStock is empty, keep the previous value
  }

  if (NEWproductMinStock) {
    formData.append("product_min_stock", NEWproductMinStock); // If there's a value in NEWproductMinStock, update the corresponding column
  } else {
    formData.append("product_min_stock", productMinStock); // If NEWproductMinStock is empty, keep the previous value
  }

  if (NEWproductCost) {
    formData.append("product_cost", NEWproductCost); // If there's a value in NEWproductCost, update the corresponding column
  } else {
    formData.append("product_cost", productCost); // If NEWproductCost is empty, keep the previous value
  }

  if (NEWproductLocation) {
    formData.append("product_location", NEWproductLocation); // If there's a value in NEWproductLocation, update the corresponding column
  } else {
    formData.append("product_location", productLocation); // If NEWproductLocation is empty, keep the previous value
  }

  if (NEWproductTypeid) {
    formData.append("product_type_id", NEWproductTypeid); // If there's a value in NEWproductTypeid, update the corresponding column
  } else {
    formData.append("product_type_id", productTypeid); // If NEWproductTypeid is empty, keep the previous value
  }

  if (NEWproductFecha) {
    formData.append("product_fecha", NEWproductFecha); // If there's a value in NEWproductFecha, update the corresponding column
  } else {
    formData.append("product_fecha", productFecha); 
  }
  const url = `/update/${productId}/`;

  fetch(url, {
    method: "POST",
    body: formData,
   
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      alert(data.message);
      
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal
    $("#editProductModal").modal("hide");

    // Limpia los parámetros
    $("#editProductForm")[0].reset();
    
    // Recarga la página
    window.location.reload();
};

function editUser() {
  const userId = $('#NEWuserId').val();
  const username = $('#username').val();
  const nombre = $('#nombre').val();
  const apellidos = $('#apellidos').val();
  const direccion = $('#direccion').val();
  const correo = $('#correo').val();
  const telefono = $('#telefono').val();
  const roleId = $('#role_id').val();
  
  const NEWusername = $('#NEWusername').val();
  const NEWnombre = $('#NEWnombre').val();
  const NEWapellidos = $('#NEWapellidos').val();
  const NEWdireccion = $('#NEWdireccion').val();
  const NEWcorreo = $('#NEWcorreo').val();
  const NEWtelefono = $('#NEWtelefono').val();
  const NEWroleId = $('#NEWrole_id').val();

  const formData = new FormData(document.getElementById("createUserForm"));

  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  if (NEWusername) {
    formData.append("username", NEWusername); // Si hay un valor en NEWusername, actualizar la columna correspondiente
  } else {
    formData.append("username", username); // Si NEWusername está vacío, mantener el valor anterior
  }
  if (NEWnombre) {
    formData.append("nombre", NEWnombre); // Si hay un valor en NEWnombre, actualizar la columna correspondiente
  } else {
    formData.append("nombre", nombre); // Si NEWnombre está vacío, mantener el valor anterior
  }
  if (NEWapellidos) {
    formData.append("apellidos", NEWapellidos); // Si hay un valor en NEWapellidos, actualizar la columna correspondiente
  } else {
    formData.append("apellidos", apellidos); // Si NEWapellidos está vacío, mantener el valor anterior
  }
  if (NEWdireccion) {
    formData.append("direccion", NEWdireccion); // Si hay un valor en NEWdireccion, actualizar la columna correspondiente
  } else {
    formData.append("direccion", direccion); // Si NEWdireccion está vacío, mantener el valor anterior
  }
  if (NEWcorreo) {
    formData.append("correo", NEWcorreo); // Si hay un valor en NEWcorreo, actualizar la columna correspondiente
  } else {
    formData.append("correo", correo); // Si NEWcorreo está vacío, mantener el valor anterior
  }
  if (NEWtelefono) {
    formData.append("telefono", NEWtelefono); // Si hay un valor en NEWtelefono, actualizar la columna correspondiente
  } else {
    formData.append("telefono", telefono); // Si NEWtelefono está vacío, mantener el valor anterior
  }
  if (NEWroleId) {
    formData.append("roleId", NEWroleId); // Si hay un valor en NEWroleId, actualizar la columna correspondiente
  } else {
    formData.append("roleId", roleId); // Si NEWroleId está vacío, mantener el valor anterior
  }

  const url = `editUser/${userId}/`;
  
  fetch(url, {
    method: "POST",
    body: formData,
   
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      alert(data.message);
      
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal
    $("#editUserModal").modal("hide");

    // Limpia los parámetros
    $("#editUserForm")[0].reset();

    window.location.reload();
};


function deleteProduct() {
  const productId = $('#productId').val();

  const url = `/delete/${productId}/`;
  
  fetch(url, {
    method: "POST",
    body: `productId=${productId}`,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": getCookie("csrftoken")
    }
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      alert(data.message + "id:" + productId);
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal
    $("#deleteProductModal").modal("hide");
  
    // Recarga la página
    location.reload();
    
};
$('#editUserButton').click(function() {
  const userId = $(this).data('user-id');
  $('#deleteUserButton').data('user-id', userId);
});

function deleteUser() {
  const userId = $('#userId').val();
  console.log(userId);
  const url = `/deleteUser/${userId}/`;
  console.log("url: "+ url);
  fetch(url, {
    method: "POST",
    body: `userId=${userId}`,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": getCookie("csrftoken")
    }
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      alert(data.message + "id:" + userId);
    })
    .catch(data => {
      console.error("men: "+ data.message);
    });
    
    // Cierra el modal
    $("#deleteUserModal").modal("hide");
    
    // Recarga la página
    location.reload();
    
};

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Get all table tabs
var tableTabs = document.querySelectorAll('.table-tab');

// Attach event listener to each link
tableTabs.forEach(function(tab) {
  tab.addEventListener('click', function() {
    // Remove active class from all tabs
    tableTabs.forEach(function(tab) {
      tab.classList.remove('active');
    });
    // Add active class to clicked tab
    this.classList.add('active');
  });
});

function showDeleteOrderModal(button) {
  var orderId = button.getAttribute("data-order-id");
  var deleteButton = document.querySelector("#deletePedidoModal .btn-danger");
  deleteButton.setAttribute("data-order-id", orderId);
}

function deleteOrder(button) {
  var orderId = button.getAttribute("data-order-id");
  var url = `/delete_order/${orderId}/`; // Asegúrate de que esta ruta coincida con la ruta en tus urlpatterns

  fetch(url, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
      },
  })
  .then((response) => {
      if (response.status === 200) {
          location.reload();
      } else {
          console.error("Error al eliminar el pedido");
      }
  })
  .catch((error) => {
      console.error("Error al eliminar el pedido:", error);
  });
}

function updateOrderStatus(orderId, statusId) {
  const url = `/update_order_status/${orderId}/${statusId}/`;

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
  })
  .then(response => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error("Error al actualizar el estado del pedido");
    }
  })
  .then(data => {
    if (data.status === "success") {
      console.log("Estado del pedido actualizado con éxito");
    } else {
      console.error("Error al actualizar el estado del pedido");
    }
  })
  .catch(error => console.error(error));
}

function redirectToPedido() {
  var tipo_envio = document.querySelector('input[name="flexRadioDefault"]:checked').value;
  var transportista = document.querySelector('input[name="flexRadioDefault2"]:checked').value;
  
  // Check if either variable is null or empty and replace it with a default value if necessary
  if (!tipo_envio || tipo_envio.trim() === '') {
    tipo_envio = '1';
  }
  if (!transportista || transportista.trim() === '') {
    transportista = '1';
  }
  console.log(tipo_envio)
  console.log(transportista)
  var url = "/cart/mandarPedido/tipo_envio/transportista";
  window.location.href = url.replace('tipo_envio', tipo_envio).replace('transportista', transportista);
}
  
function deleteProductProveedor(button) {
  var productId = button.getAttribute("data-product-id2");
  var url = `/eliminar_producto_pedido/${productId}/`;

  fetch(url, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
      },
  })
  .then((response) => {
      if (response.status === 200) {
          location.reload();
      } else {
          console.error("Error al eliminar el producto");
      }
  })
  .catch((error) => {
      console.error("Error al eliminar el producto:", error);
  });
}

