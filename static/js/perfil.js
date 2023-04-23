document.addEventListener("DOMContentLoaded", function() {
    const datos = document.getElementById("selectDatos");
    const pedidos = document.getElementById("selectPedidos");
    const infoDatos = document.getElementById("infoDatos");
    const infoPedidos = document.getElementById("infoPedidos");
    
    datos.addEventListener("click", function() {
        infoDatos.classList.remove("perfilHide");
        infoPedidos.classList.add("perfilHide");
    });
    pedidos.addEventListener("click", function() {
        infoDatos.classList.add("perfilHide");
        infoPedidos.classList.remove("perfilHide");
    });
});