$(document).ready(function() {
    $("#product-type").change(function(){
      var selectedValue = this.value;
      console.log("Valor seleccionado: " + selectedValue);
      console.log("Evento cambiado");
      // Hacer una llamada AJAX a tu vista de Django para actualizar los productos
      $.ajax({
        url: 'filtroInicio/' + selectedValue,
        type: 'GET',
        success: function(data) {
          var htmlString = $( "div.here" ).html(" {% for queryType in query %} <div{{ queryType.name }}</div>   {% endfor %}");
          console.log("valor:" + htmlString)
          // Actualizar el HTML con los nuevos productos
          
          $("#here").html(data);
          }
      });
    });
  });

