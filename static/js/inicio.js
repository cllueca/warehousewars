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
  selected = false;
  $("#product-type").change(function(){
    let selectedValue = this.value;
    selected = true;
  fetch(`http://127.0.0.1:8000/filtroInicio/${selectedValue}/`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Status code error: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
          //aqui recibiras el json y puedes mostrarlo en tu vista
          console.log(selectedValue);
          let productos = data;
          let contenedor = document.getElementById("here")
          while (contenedor.firstChild) {
            contenedor.removeChild(contenedor.firstChild);
          }
          contenedor.innerHTML = "";
          console.log(contenedor);
          for (let i = 0; i < productos.length; i++) {
            contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info"  id="product-${productos[i].product_id}" data-product-id="${productos[i].product_id}">
            <div class="card" >
              <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
              <hr>
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
  });
});

document.addEventListener("DOMContentLoaded", function() {
 $("#product-prize").change(function(){
    let selectedPrize = this.value;
    console.log(selectedPrize);
    selected = true;
  fetch(`http://127.0.0.1:8000/filtroPrecio/${selectedPrize}/`)
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
            contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info" id="product-${productos[i].product_id}" data-product-id="${productos[i].product_id}">
            <div class="card" >
              <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
              <hr>
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
  });
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

document.addEventListener("DOMContentLoaded", function() {
  $("#product-proveedor").change(function(){
     let selectedProveedor = this.value;
     console.log(selectedProveedor);
     selected = true;
   fetch(`http://127.0.0.1:8000/filtroProveedor/${selectedProveedor}/`)
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
             contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info" id="product-${productos[i].product_id}" data-product-id="${productos[i].product_id}">
             <div class="card" >
               <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
               <hr>
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
          contenedor.innerHTML += `<div class="col-md-4 mt-4 product-info" id="product-${productos[i].product_id}" data-product-id="${productos[i].product_id}">
          <div class="card" >
            <img src="${productos[i].image_url}" class="imageCard card-img-top mx-auto d-block"  alt="#" >
            <hr>
            <div class="card-body d-flex justify-content-between">
              <div>
                <h5 class="card-title">${productos[i].name}</h5>
              </div>
              <div class="text-right">
                <p class="card-text">${productos[i].cost_per_unit}</p>
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

