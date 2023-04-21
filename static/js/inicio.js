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
    url = `http://127.0.0.1:8000/filtroInicio/${selectedValue}/`
    $("#product-prize, #product-proveedor").val("0").change();
    updateProducts(url);
    }
  });

  $("#product-prize").change(function() {
    selectedPrize = this.value;
    if (selectedPrize != "0") {
    selected = true;
    url =`http://127.0.0.1:8000/filtroPrecio/${selectedPrize}/`
    $("#product-type, #product-proveedor").val("0").change();
    updateProducts(url);
    }
  });

  $("#product-proveedor").change(function() {
    selectedProveedor = this.value;
    if (selectedProveedor != "0") {
    selected = true;
    url = `http://127.0.0.1:8000/filtroProveedor/${selectedProveedor}/`
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
              <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block" alt="#">
              <hr style="border-color: #FEA424;">
              <div class="card-body d-flex justify-content-between">
                <div>
                  <h5 class="card-title">${productos[i].name}</h5>
                </div>
                <div class="text-right">
                  <p class="card-text borderPrize">${productos[i].cost_per_unit}</p>
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

    fetch(`http://127.0.0.1:8000/showmore/`)
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
<<<<<<< HEAD
            <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
=======
            <img src="${productos[i].image}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
>>>>>>> origin/branchDiego
            <hr style="border-color: #FEA424;">
            <div class="card-body d-flex justify-content-between">
              <div>
                <h5 class="card-title">${productos[i].name}</h5>
              </div>
              <div class="text-right">
                <p class="card-text">${productos[i].price}</p>
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

<<<<<<< HEAD
function updateProduct() {
  const productId = $('#productId').val();

  const formData = new FormData(document.getElementById("editProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);

  const url = `/update/${productId}/`;

  fetch(url, {
    method: "POST",
    body: formData
=======

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
   
>>>>>>> origin/branchDiego
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error en la respuesta, estado: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
<<<<<<< HEAD
      // handle response data
=======
      alert(data.message);
>>>>>>> origin/branchDiego
    })
    .catch(data => {
      console.error(data.message);
    });
    
    // Cierra el modal
<<<<<<< HEAD
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

function createProduct() {

  const formData = new FormData(document.getElementById("createProductForm"));
  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  
  const url = `/create/`;
=======
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
>>>>>>> origin/branchDiego
  
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
<<<<<<< HEAD
    $("#createProductModal").modal("hide");

    // Limpia los parámetros
    $("#createProductForm")[0].reset();
=======
    $("#createUserModal").modal("hide");

    // Limpia los parámetros
    $("#createUserForm")[0].reset();

    
    // Recarga la página
    location.reload();
>>>>>>> origin/branchDiego
};

$(document).ready(function () {
  $('.btn-danger').click(function () {
  var productId = $(this).data('product-id');
  $('#productId').val(productId);
<<<<<<< HEAD
  });
});

=======
  var userId = $(this).data('user-id');
  $('#userId').val(userId);
  });
});

$(document).ready(function () {
  $('.btn-warning').click(function () {
  var productId = $(this).data('product-id');
  $('#productId').val(productId);
  var productName = $(this).data('product-name');
  $('#productName').val(productName);
  var productStock= $(this).data('product-stock');
  $('#productStock').val(productStock);
  var productMinStock= $(this).data('product-minstock');
  $('#productMinStock').val(productMinStock);
  var productCost= $(this).data('product-cost');
  $('#productCost').val(productCost);
  var productLocation= $(this).data('product-location');
  $('#productTypeid').val(productLocation);
  var productTypeid = $(this).data('product-typeid');
  $('#productTypeid').val(productTypeid);
  var productFecha = $(this).data('product-fecha');
  $('#productFecha').val(productFecha);

  console.log(productId)
  console.log(productName)
  console.log(productStock)
  console.log(productMinStock) 
  console.log(productCost)
  console.log(productLocation)
  console.log(productTypeid)
  console.log(productFecha)
  var userId = $(this).data('user-id');
  $('#userId').val(userId);
  var username = $(this).data('username');
  $('#username').val(username);
  var nombre = $(this).data('nombre');
  $('#nombre').val(nombre);
  var apellidos = $(this).data('apellidos');
  $('#apellidos').val(apellidos);
  var direccion = $(this).data('direccion');
  $('#direccion').val(direccion);
  var correo = $(this).data('correo');
  $('#correo').val(correo);
  var telefono = $(this).data('telefono');
  $('#telefono').val(telefono);
  var roleId = $(this).data('role-id');
  $('#role_id').val(roleId);
  var password = $(this).data('password');
  $('#password').val(password);
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

  console.log(productId)
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
    //$("#editProductModal").modal("hide");

    // Limpia los parámetros
    //$("#editProductForm")[0].reset();
    
    // Recarga la página
    //window.location.reload();
};

function editUser() {
  const userId = $('#userId').val();
  const username = $('#username').val();
  const password = $('#password').val();
  const nombre = $('#nombre').val();
  const apellidos = $('#apellidos').val();
  const direccion = $('#direccion').val();
  const correo = $('#correo').val();
  const telefono = $('#telefono').val();
  const roleId = $('#role_id').val();
  
  const NEWusername = $('#NEWusername').val();
  const NEWpassword = $('#NEWpassword').val();
  const NEWnombre = $('#NEWnombre').val();
  const NEWapellidos = $('#NEWapellidos').val();
  const NEWdireccion = $('#NEWdireccion').val();
  const NEWcorreo = $('#NEWcorreo').val();
  const NEWtelefono = $('#NEWtelefono').val();
  const NEWroleId = $('#NEWrole_id').val();
  /*console.log(NEWusername)
  console.log(NEWpassword)
  console.log(NEWnombre)
  console.log(NEWapellidos) 
  console.log(NEWdireccion)
  console.log(NEWcorreo)
  console.log(NEWtelefono)
  console.log(NEWroleId)*/
  const formData = new FormData(document.getElementById("createUserForm"));

  const csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  formData.append("csrfmiddlewaretoken", csrf_token);
  if (NEWusername) {
    formData.append("username", NEWusername); // Si hay un valor en NEWusername, actualizar la columna correspondiente
  } else {
    formData.append("username", username); // Si NEWusername está vacío, mantener el valor anterior
  }
  if (NEWpassword !== password || NEWpassword === "") {
    formData.append("password", NEWpassword); // Si son diferentes, actualizar la columna correspondiente
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

  const url = `/editUser/${userId}/`;
  
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


>>>>>>> origin/branchDiego
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
<<<<<<< HEAD
=======
  
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
>>>>>>> origin/branchDiego
    
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
<<<<<<< HEAD
=======

/*CRUD*/
$(document).ready(function() {
  const product_checkbox = $('#producto-checkbox');
  const CRUDproduct = $('#CRUDproduct');

  const user_checkbox = $('#user-checkbox');
  const CRUDuser = $('#CRUDuser');

  const pedido_checkbox = $('#pedido-checkbox');
  const CRUDpedido = $('#CRUDpedido');

  const pedidoProv_checkbox = $('#pedidoProv-checkbox');
  const CRUDpedidoProv = $('#CRUDpedidoProv');
  
  product_checkbox.change(function(){
    if ($(this).is(':checked')) {
      CRUDproduct.show();
    } else {
      CRUDproduct.hide();
    }
  });

  user_checkbox.change(function(){
    if ($(this).is(':checked')) {
      CRUDuser.show();
    } else {
      CRUDuser.hide();
    }
  });

  pedido_checkbox.change(function(){
    if ($(this).is(':checked')) {
      CRUDpedido.show();
    } else {
      CRUDpedido.hide();
    }
  });

  pedidoProv_checkbox.change(function(){
    if ($(this).is(':checked')) {
      CRUDpedidoProv.show();
    } else {
      CRUDpedidoProv.hide();
    }
  });
});
>>>>>>> origin/branchDiego