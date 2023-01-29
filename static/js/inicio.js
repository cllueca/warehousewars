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
      .then(response => response.json())
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
            contenedor.innerHTML += `<div class="col-md-4 mt-4" >
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
            contenedor.innerHTML += `<div class="col-md-4 mt-4" >
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
      });
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
             contenedor.innerHTML += `<div class="col-md-4 mt-4" >
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
       });
   });
 });

$(document).ready(function() {
  $('.product-info').click(function() {
    var $element = $(this);
    var productId = $element.data('product-id');
    console.log("Valor id: " + productId)
    location.href = '/descProducto/' + productId + '/'; 
  });
});
 //location.href = '/descProducto/' + productId + '/';    onclick="location.href='/descProducto/' + this.dataset.productId + '/'"