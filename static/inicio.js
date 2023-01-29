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
  document.querySelector("#product-type").addEventListener("click", function() {
    let selectedValue = this.value;
  if(selectedValue!=""){
  fetch(`http://127.0.0.1:8000/filtroInicio/${selectedValue}/`)
      .then(response => response.json())
      .then(data => {
          //aqui recibiras el json y puedes mostrarlo en tu vista
          console.log(data);
          let productos = data;
          let contenedor = document.getElementById("here")
          contenedor.innerHTML = "";
          console.log(productos);
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
  }else{
    fetch(`http://127.0.0.1:8000/filtroInicio/`)
        .then(response => response.json())
        .then(data => {
            //aqui recibiras el json y puedes mostrarlo en tu vista
            console.log(data);
        });
  }
  });
});


