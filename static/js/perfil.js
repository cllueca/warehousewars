document.addEventListener("DOMContentLoaded", function() {
    const datos = document.getElementById("selectDatos");
    const pedidos = document.getElementById("selectPedidos");
    const infoDatos = document.getElementById("infoDatos");
    const infoPedidos = document.getElementById("infoPedidos");
    
    datos.addEventListener("click", function() {
        infoDatos.classList.toggle("perfilHide");
        infoPedidos.classList.toggle("perfilHide");
    });
    pedidos.addEventListener("click", function() {
        infoDatos.classList.toggle("perfilHide");
        infoPedidos.classList.toggle("perfilHide");
    });
});


// $(document).ready(function() {
//     // Mostrar información de datos al cargar la página
//     $("#datos").show();
//     $("#pedidos").hide();

//     // Al hacer clic en el botón "Datos"
//     $("[href='#datos']").click(function() {
//         alert("Hola");
//         $("#datos").show();
//         $("#pedidos").hide();
//         $("[href='#datos']").addClass("perfilActive");
//         $("[href='#pedidos']").removeClass("perfilHide");
//     });

//     // Al hacer clic en el botón "Pedidos"
//     $("[href='#pedidos']").click(function() {
//         $("#datos").hide();
//         $("#pedidos").show();
//         $("[href='#pedidos']").addClass("perfilHide");
//         $("[href='#datos']").removeClass("perfilActive");
//     });
// });