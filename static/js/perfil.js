document.addEventListener("DOMContentLoaded", function() {
    const datos = document.getElementById("selectDatos");
    const pedidos = document.getElementById("selectPedidos");
    const infoDatos = document.getElementById("infoDatos");
    const infoPedidos = document.getElementById("infoPedidos");
    
    datos.addEventListener("click", function() {
        infoDatos.classList.remove("perfilHide");
        infoPedidos.classList.add("perfilHide");
        datos.classList.add('active');
        pedidos.classList.remove('active');
    });
    pedidos.addEventListener("click", function() {
        infoDatos.classList.add("perfilHide");
        infoPedidos.classList.remove("perfilHide");
        datos.classList.remove('active');
        pedidos.classList.add('active');
    });
});