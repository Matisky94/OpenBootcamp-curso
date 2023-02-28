document.getElementById("expandir_1").addEventListener("click", function() {
    document.getElementById("sous_chef_1").style.display = "block"
    document.getElementById("sous_chef_2").style.display = "block"
    document.getElementById("expandir_1").style.display = "none"
    document.getElementById("ocultar_1").style.display = "block"
})

document.getElementById("ocultar_1").addEventListener("click", function() {
    document.getElementById("sous_chef_1").style.display = "none"
    document.getElementById("sous_chef_2").style.display = "none"
    document.getElementById("ocultar_1").style.display = "none"
    document.getElementById("expandir_1").style.display = "block"
})

document.getElementById("expandir_2").addEventListener("click", function() {
    document.getElementById("expenditer_1").style.display = "block"
    document.getElementById("expenditer_2").style.display = "block"
    document.getElementById("expandir_2").style.display = "none"
    document.getElementById("ocultar_2").style.display = "block"
})

document.getElementById("ocultar_2").addEventListener("click", function() {
    document.getElementById("expenditer_1").style.display = "none"
    document.getElementById("expenditer_2").style.display = "none"
    document.getElementById("ocultar_2").style.display = "none"
    document.getElementById("expandir_2").style.display = "block"
})

document.getElementById("expandir_3").addEventListener("click", function() {
    document.getElementById("cocinero_1").style.display = "block"
    document.getElementById("cocinero_2").style.display = "block"
    document.getElementById("cocinero_3").style.display = "block"
    document.getElementById("expandir_3").style.display = "none"
    document.getElementById("ocultar_3").style.display = "block"
})

document.getElementById("ocultar_3").addEventListener("click", function() {
    document.getElementById("cocinero_1").style.display = "none"
    document.getElementById("cocinero_2").style.display = "none"
    document.getElementById("cocinero_3").style.display = "none"
    document.getElementById("ocultar_3").style.display = "none"
    document.getElementById("expandir_3").style.display = "block"
})

document.getElementById("expandir_4").addEventListener("click", function() {
    document.getElementById("pantry_1").style.display = "block"
    document.getElementById("pantry_2").style.display = "block"
    document.getElementById("expandir_4").style.display = "none"
    document.getElementById("ocultar_4").style.display = "block"
})

document.getElementById("ocultar_4").addEventListener("click", function() {
    document.getElementById("pantry_1").style.display = "none"
    document.getElementById("pantry_2").style.display = "none"
    document.getElementById("ocultar_4").style.display = "none"
    document.getElementById("expandir_4").style.display = "block"
})

document.getElementById("color").addEventListener("click", function() {
    document.body.style.backgroundColor = "grey"
    document.getElementById("cambiar_color").style.display = "none"
    document.getElementById("reset_color").style.display = "block"
})

document.getElementById("restaurar").addEventListener("click", function() {
    document.body.style.backgroundColor = "white"
    document.getElementById("cambiar_color").style.display = "block"
    document.getElementById("reset_color").style.display = "none"
})