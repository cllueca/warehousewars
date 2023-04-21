document.addEventListener("DOMContentLoaded", function() {
    const datos = document.getElementById("selectDatos");
    const infoDatos = document.getElementById("infoDatos");
    
    datos.addEventListener("mouseenter", function() {
        this.size = this.options.length + 2.2;
        select.style.transform = "scale(1.1)";
        this.style.color = "black";
    });
    datos.addEventListener("mouseleave", function() {
        this.size = 1;
        select.style.transform = "scale(1)";
        select.style.overflow = "hidden";
        this.style.color = "black";
    });
});


// $(document).ready(function() {
//     // Mostrar información de datos al cargar la página
//     $("#datos").show();
//     $("#pedidos").hide();

//     // Al hacer clic en el botón "Datos"
//     $("[href='#datos']").click(function() {
//         $("#datos").show();
//         $("#pedidos").hide();
//         $("[href='#datos']").addClass("active");
//         $("[href='#pedidos']").removeClass("active");
//     });

//     // Al hacer clic en el botón "Pedidos"
//     $("[href='#pedidos']").click(function() {
//         $("#datos").hide();
//         $("#pedidos").show();
//         $("[href='#pedidos']").addClass("active");
//         $("[href='#datos']").removeClass("active");
//     });
// });