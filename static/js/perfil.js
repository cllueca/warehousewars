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