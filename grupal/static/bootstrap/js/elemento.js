

function get_url(){
let url = window.location.href;
sessionStorage.setItem("busq1", url);
console.log(url)
}


function getElements(){
var nombre_profesor = document.getElementById('userProfesor').value
var carrera = document.getElementById('sel').value
var elementos = "busqueda1/"+ carrera + '/' + nombre_profesor;
var url = sessionStorage.getItem("busq1");
var url = url + elementos ;
window.location.replace(url)
}

function buscar1(){
var nombre_profesor = document.getElementById('userProfesor').value;
var carrera = document.getElementById('sel').value;
var curso = document.getElementById('cur').value;
var elementos = "buscar1/"+ carrera + '/' + nombre_profesor + '/' + curso;
var url = sessionStorage.getItem("busq1");
var url = url + elementos ;
let busqueda = url;
sessionStorage.setItem("bd", busqueda);
}

function mandarBusqueda(){
var nombre_profesor = document.getElementById('userProfesor').value;
var curso = document.getElementById('cur').value;
console.log(curso)
if (nombre_profesor == ""){
    swal('Porfavor escribe el profesor')
}else if (curso == "Curso"){
    swal('Porfavor seleccione el curso')
}else{
    var url = sessionStorage.getItem("bd");
    window.location.replace(url)
}

}


function validar(){
var nombre_profesor = document.getElementById('userProfesor').value;

if (nombre_profesor == ""){
    swal('Porfavor escribe el profesor')
}else{
    swal('Porfavor seleccione los dos filtros')
}
}

function obtener_cita(citaHtml){
var cita = citaHtml
var elementos = "asesoria/"+ cita.profesor__nombre_profesor+"/"+cita.dia+"/"+cita.lugar+"/"+cita.hora_inicio+"/"+cita.hora_fin;
var url = sessionStorage.getItem("busq1");
var url = url + elementos ;
let busqueda = url;
sessionStorage.setItem("bd", busqueda);
console.log(busqueda)
}

function reservaSel(){
var url = sessionStorage.getItem("bd");
window.location.replace(url)
}
