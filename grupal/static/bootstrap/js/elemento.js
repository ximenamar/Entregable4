//Sesión
function getBase(){
  let base = window.location.href;
  let main = base.split("inicio/login/")
  sessionStorage.setItem("urlProf",main[0]+ "principal");
  sessionStorage.setItem("ini",0);
}

function getTipo(tipo){
  var url = sessionStorage.getItem("urlProf");

  if (tipo == "profesor") {
    var url = url+"/p/"
    window.location.replace(url);
  }else if (tipo == "administrador") {
    var url = url+"/a/"
    window.location.replace(url);
  }else {
    window.location.replace(url);
  }
}
//Notificaciones
function noti(user,tipo){
var ini = sessionStorage.getItem("ini");
  console.log(user);
  if (ini == 0) {
    const inicio = swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000
    });
    inicio({
      type: 'success',
      title: 'Sesión iniciada, '+tipo+' '+user
    })
    sessionStorage.setItem("ini",1);
  }
}
function aseR(user,tipo){
var ini = sessionStorage.getItem("ini");
if (ini==2) {
  const inicio = swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000
  });
  inicio({
    type: 'success',

    title: 'Asesoría reservada, '+tipo+' '+user
  })
  sessionStorage.setItem("ini",1);
}

}

//Alumno

function inicio(){
var url = sessionStorage.getItem("busq1");
window.location.replace(url);
}

function regresarFilt(){
var url = sessionStorage.getItem("busq1");
var url = url +"busqueda1/";
window.location.replace(url);
}

function regresarEtiq(){
var url = sessionStorage.getItem("busq1");
var url = url +"busqueda2/";
window.location.replace(url);
}

function get_url(usu){
let usuario = usu
let url = window.location.href;
console.log(usuario)
sessionStorage.setItem("busq1", url);
sessionStorage.setItem("usu", usuario);
sessionStorage.setItem("urlProf",url);
}

function get_usu(usu){
let usuario = usu
let url = window.location.href;
sessionStorage.setItem("busq1", url);
sessionStorage.setItem("usu", usuario);
var elementos = "ver/"+ usuario;
var ver = sessionStorage.getItem("busq1");
var ver = url + elementos ;
window.location.replace(ver);
}

function getElements(){
var nombre_profesor = document.getElementById('userProfesor').value
console.log(nombre_profesor);
var carrera = document.getElementById('sel').value
var elementos = "busqueda1/"+ carrera + '/' + nombre_profesor;
var url = sessionStorage.getItem("busq1");
var url = url + elementos ;
if (nombre_profesor != "") {
  window.location.replace(url)
}else {
  const swalWithBootstrapButtons = swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    allowOutsideClick: true,
  })
  swalWithBootstrapButtons({
    title: '¡Espere!',
    text: 'Escriba el profesor',
    type: 'warning',
    confirmButtonColor: '#3085d6',
    confirmButtonText: 'ok'
  }).then((result) => {
    if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.acept) {
      location.reload();
    }
  })

}

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

function mandarBusqueda(usu){
var nombre_profesor = document.getElementById('userProfesor').value;
var curso = document.getElementById('cur').value;
console.log(curso)
if (nombre_profesor == ""){
  swal("¡Espere!", 'Porfavor escribe el profesor', "warning");
}else if (curso == "Curso"){
  swal("¡Espere!", 'Porfavor seleccione el curso', "warning");
}else{
    var url = sessionStorage.getItem("bd");
    var url = url +"/" +usu;
    window.location.replace(url);
}

}


function validar(){
var nombre_profesor = document.getElementById('userProfesor').value;

if (nombre_profesor == ""){
  swal("¡Espere!", 'Porfavor escribe el profesor', "warning");

}else{
  swal("¡Espere!", 'Porfavor seleccione los dos filtros', "warning");
}
}

function obtener_cita(citaHtml){
var cita = citaHtml;
var alumno = sessionStorage.getItem("usu");
var elementos = "asesoria/"+ cita.profesor__nombre_profesor+"/"+alumno+"/"+cita.dia+"/"+cita.lugar+"/"+cita.hora_inicio+"/"+cita.hora_fin;
var url = sessionStorage.getItem("busq1");
var url = url + elementos ;
let busqueda = url;
sessionStorage.setItem("bd", busqueda);

console.log(busqueda)
}

function restaurarBD(){
  var reusar = "#"
  sessionStorage.setItem("bd",reusar)
}

function reservaSel(){
sessionStorage.setItem("ini",2);
var no = [];
var or = document.getElementById("no");
no.push(or);
console.log(no);
var url = sessionStorage.getItem("bd");
var reusar = "#"
if (no[0] != null) {
  swal("¡Error!", 'No existen asesorías', "error");
}else if (url != "#"){
  sessionStorage.setItem("bd",reusar)
  window.location.replace(url)
}else{
  swal("¡Espere!", 'Porfavor seleccione la asesoría', "warning");
}
}

function reservaSelE(no){
sessionStorage.setItem("ini",2);
var noE = [no];
console.log(noE);
var url = sessionStorage.getItem("bd");
var reusar = "#"

if (noE[0] != "") {
  swal("¡Error!", 'No existen asesorías', "error");
}else if (url != "#"){
  sessionStorage.setItem("bd",reusar)
  window.location.replace(url)
}else{
  swal("¡Espere!", 'Porfavor seleccione la asesoría', "warning");
}
}


function aceptar(){
  var url = sessionStorage.getItem("busq1");
  window.location.replace(url);
}

function retornar(alumn){
  var url = sessionStorage.getItem("busq1");
  var url = url + "ver"+"/"+alumn;
  window.location.replace(url);
}

function reservaCancel(asesoria){
aseCancel = asesoria.asesoria
var url = sessionStorage.getItem("busq1");

const swalWithBootstrapButtons = swal.mixin({
  confirmButtonClass: 'btn btn-success',
  cancelButtonClass: 'btn btn-danger',
  confirmButtonColor: '#d33',
  cancelButtonColor: '#3085d6',
  allowOutsideClick: true,
})

swalWithBootstrapButtons({
  title: '¿Está seguro?',
  text: "Se va a cancelar la cita",
  type: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Sí, ¡Cancélala!',
  cancelButtonText: 'No',
  reverseButtons: true
}).then((result) => {
  if (result.value) {
    $.get('/principal/asesoria/cancelar/'+aseCancel,function(){
      swalWithBootstrapButtons({
        title: '¡Se ha borrado la cita!',
        type: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'ok'
      }).then((result) => {
        if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.acept) {
          var url = sessionStorage.getItem("busq1");
          var url = url + "ver"+"/"+asesoria.alumno__nombre_alumno;
          window.location.replace(url);
        }
      })
    })
  } else if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.cancel) {
    swalWithBootstrapButtons(
      '¡No se ha borrado la cita!',
      '',
      'info'
    )
  }
})

}

function reservaReAceptar(asesoria){
aseReCrear = asesoria.asesoria
var url = sessionStorage.getItem("busq1");

const swalWithBootstrapButtons = swal.mixin({
  confirmButtonClass: 'btn btn-success',
  cancelButtonClass: 'btn btn-danger',
  confirmButtonColor: '#d33',
  cancelButtonColor: '#3085d6',
  allowOutsideClick: true,
})

swalWithBootstrapButtons({
  title: '¿Está seguro?',
  text: "Se va a reenviar la cita",
  type: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Sí, ¡Pídela!',
  cancelButtonText: 'No',
  reverseButtons: true
}).then((result) => {
  if (result.value) {
    $.get('/principal/asesoria/'+aseReCrear,function(){
      swalWithBootstrapButtons({
        title: '¡Se ha pedido la reserva de cita nuevamente!',
        type: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'ok'
      }).then((result) => {
        if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.acept) {
          var url = sessionStorage.getItem("busq1");
          var url = url + "ver"+"/"+asesoria.alumno__nombre_alumno;
          window.location.replace(url);
        }
      })
    })
  } else if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.cancel) {
    swalWithBootstrapButtons(
      '¡No se ha reenviado la cita!',
      '',
      'info'
    )
  }
})
}

function mostrarAsesoria(asesoria){
var ver = sessionStorage.getItem("busq1");
if (asesoria.estado == "pendiente a aceptar" || asesoria.estado == "aceptada" ){
  var elementos = "asesoria/"+asesoria.profesor__nombre_profesor+"/"+asesoria.alumno__nombre_alumno+"/"+asesoria.dia+"/"+asesoria.lugar+"/"+asesoria.hora_inicio+"/"+asesoria.hora_fin;

}else {
  var elementos = "asesoria/"+asesoria.profesor__nombre_profesor+"/"+asesoria.alumno__nombre_alumno+"/"+asesoria.dia+"/"+asesoria.lugar+"/"+asesoria.hora_inicio+"/"+asesoria.hora_fin+"/"+asesoria.estado;
}
var ver = ver + elementos ;
window.location.replace(ver);

}

//Profesor

function get_prof(prof){
let usuario = prof
let url = window.location.href;
sessionStorage.setItem("busq1", url);
sessionStorage.setItem("usu", usuario);
var elementos = "ver/"+ usuario;
var ver = sessionStorage.getItem("busq1");
var ver = url + elementos ;
window.location.replace(ver);
}

function mostrarAsesoriaProf(asesoria){
var ver = sessionStorage.getItem("busq1");
if (asesoria.estado == "pendiente a aceptar") {
  var elementos = "asesoria/"+asesoria.profesor__nombre_profesor+"/"+asesoria.alumno__nombre_alumno+"/"+asesoria.dia+"/"+asesoria.lugar+"/"+asesoria.hora_inicio+"/"+asesoria.hora_fin;
}else {
  var elementos = "asesoria/"+asesoria.profesor__nombre_profesor+"/"+asesoria.alumno__nombre_alumno+"/"+asesoria.dia+"/"+asesoria.lugar+"/"+asesoria.hora_inicio+"/"+asesoria.hora_fin+"/"+asesoria.estado;
}
var ver = ver + elementos ;
window.location.replace(ver);
}

function reservaAceptar(asesoria){
aseAceptar = asesoria.asesoria
var url = sessionStorage.getItem("busq1");

const swalWithBootstrapButtons = swal.mixin({
  confirmButtonClass: 'btn btn-success',
  cancelButtonClass: 'btn btn-danger',
  confirmButtonColor: '#d33',
  cancelButtonColor: '#3085d6',
  allowOutsideClick: true,
})

swalWithBootstrapButtons({
  title: '¿Está seguro sobre aceptar?',
  text: "Se va a aceptar la cita con el alumno",
  type: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Sí, ¡Acéptala!',
  cancelButtonText: 'No',
  reverseButtons: true
}).then((result) => {
  if (result.value) {
    $.get('/principal/p/asesoria/aceptar/'+aseAceptar,function(){
      swalWithBootstrapButtons({
        title: '¡Se ha aceptado la cita!',
        type: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'ok'
      }).then((result) => {
        if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.acept) {
	  var url = sessionStorage.getItem("busq1");
          var url = url + "ver"+"/"+asesoria.profesor__nombre_profesor;
          window.location.replace(url);
        }
      })
    })
  } else if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.cancel) {
    swalWithBootstrapButtons(
      '¡No se ha aceptado la cita!',
      '',
      'info'
    )
  }
})

}

function reservaNoAceptar(asesoria){
aseNoAceptar = asesoria.asesoria
var url = sessionStorage.getItem("busq1");
swal({
  title: "¿Está seguro sobre no aceptar?",
  text: "Se va a eliminar lo aceptado con el alumno",
  type: "warning",
  buttons: true,
  dangerMode: true,
})
.then((willDelete) => {
  if (willDelete) {
    $.get('/principal/p/asesoria/noaceptar/'+aseNoAceptar,function(){
      swal({
        title: "¡Se ha eliminado lo aceptado !",
        type: "success",
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          var url = sessionStorage.getItem("busq1");
          var url = url + "ver"+"/"+asesoria.profesor__nombre_profesor;
          window.location.replace(url);
        }
      });
    })

  } else {
    swal({
      title: "¡Se sigue aceptando la cita!",
      type: "info",
    })
  }
});

}

function regresar(prof){
  var url = sessionStorage.getItem("busq1");
  var url = url + "ver"+"/"+prof;
  window.location.replace(url);
}

function crearProf(prof,tipo){
  $.get('/principal/p/guardarProf/'+prof,function(){
  })
  var ini = sessionStorage.getItem("ini");
    if (ini == 0) {
      const inicio = swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
      });
      inicio({
        type: 'success',
        title: 'Sesión iniciada, '+tipo+' '+prof
      })
      sessionStorage.setItem("ini",1);
    }
}

//administrador

function crearAdmin(admin,tipo){
  $.get('/principal/a/guardarAdmin/'+admin,function(){
  })
  var ini = sessionStorage.getItem("ini");
    if (ini == 0) {
      const inicio = swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
      });
      inicio({
        type: 'success',
        title: 'Sesión iniciada, '+tipo+' '+admin
      })
      sessionStorage.setItem("ini",1);
    }
}

function crearAse(admin){
  var url = sessionStorage.getItem("urlProf");
  var url = url + "/a"+"/crearAse/"+admin;
  window.location.replace(url);
}

function queVer(){
  const {value: fruit} = swal({
    title: '¿Cómo desea gestionar los horarios?',
    input: 'select',
    inputOptions: {
      'profe': 'Profesor',
      'dia': 'Día',
    },
    inputPlaceholder: 'Selecciona profesor o día',
    showCancelButton: true,
    inputValidator: (value) => {
      return new Promise((resolve) => {
        if (value === '') {
          resolve('Seleccione, porfavor')
        } else if (value === 'profe') {
          var url = sessionStorage.getItem("urlProf");
          var url = url + "/a"+"/gestAse/"+"prof";
          window.location.replace(url);
        }else {
          var url = sessionStorage.getItem("urlProf");
          var url = url + "/a"+"/gestAse/"+"dia";
          window.location.replace(url);
        }
      })
    }
  })
}

function mostrarHora(cita){
  prof =cita.profesor__nombre_profesor
  dia =cita.dia
  let main = window.location.href;
  sessionStorage.setItem("reg",main);
  console.log(prof);
  console.log(dia);
  if (dia == undefined) {
    var url = sessionStorage.getItem("urlProf");
    var url = url + "/a"+"/gestAse/"+"ver/"+prof;
    window.location.replace(url);
  }else {
    var url = sessionStorage.getItem("urlProf");
    var url = url + "/a"+"/gestAse/"+"ver/"+dia;
    window.location.replace(url);
  }

}

function inicioA(){
var url = sessionStorage.getItem("urlProf");
var url = url+"/a/"
window.location.replace(url)
}

function  regresarA(){
var url = sessionStorage.getItem("reg");
window.location.replace(url)
}

function adminAse(){
var profesor = document.getElementById('sel').value;
var inicio = document.getElementById('inicio').value;
var fin = document.getElementById('fin').value;
var dia = document.getElementById('dia').value;
var lugar = document.getElementById('lugar').value;

if (profesor == "Profesor" || inicio == "" || fin == "" || dia == "" || lugar == "") {
  swal("¡Espere, administrador!", 'Porfavor complete todos los campos', "warning");
}else {
  var elementos = "/"+profesor+"/"+inicio+"/"+fin+"/"+dia+"/"+lugar+"/"+"cita"+profesor+inicio+lugar+dia
  swal({
    title: "¿Está seguro administrador?",
    text: "Se va a crear un horario para el profesor",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      $.get('/principal/a/asesoriaCrear'+elementos,function(resp){
        if (resp == "ok") {
          swal({
            title: "¡Se ha creado el horario!",
            icon: "success",
            dangerMode: true,
          })
          .then((willDelete) => {
            if (willDelete) {
              var url = sessionStorage.getItem("urlProf");
              var url = url + "/a/";
              window.location.replace(url);
            }
          });
        }else if (resp == "") {
          swal({
            title: "¡El horario ya existe!",
            text: "Intente con otro horario",
            icon: "error",
          })
        }else {
          swal({
            title: "¡Imposible administrador!",
            text: "No se puede exceder de dos asesorias por día",
            icon: "error",
          })
        }
      })

    } else {
      swal({
        title: "¡No se ha creado el horario!",
        icon: "info",
      })
    }
  });
}
}

function eliminarHo(cita){
  const swalWithBootstrapButtons = swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    allowOutsideClick: true,
  })

swalWithBootstrapButtons({
  title: 'Administrador, ¿Está seguro?',
  text: "Se va a eliminar el horario",
  type: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Sí, ¡Elimínalo!',
  cancelButtonText: 'No',
  reverseButtons: true
}).then((result) => {
  if (result.value) {
    $.get('/principal/a/elimiAse/'+ cita.codigo_simple,function(){
      swalWithBootstrapButtons({
        title: '¡Se ha eliminado el horario!',
        type: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'ok'
      }).then((result) => {
        if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.acept) {
	  location.reload();
        }
      })
    })
  } else if (result.dismiss === swal.DismissReason.backdrop ||result.dismiss === swal.DismissReason.cancel) {
    swalWithBootstrapButtons(
      '¡No se ha eliminado el horario!',
      '',
      'info'
    )
  }
})
}

function mostrarMod(cita){
  let main = window.location.href;
  sessionStorage.setItem("reg2",main);
  var url = sessionStorage.getItem("urlProf");
  var url = url + "/a/modAse/"+cita.codigo_simple;
  window.location.replace(url);
}

function  regresarAM(){
var url = sessionStorage.getItem("reg2");
window.location.replace(url)
}

function modificarHo(cita){
  var profesor = cita.profesor__nombre_profesor
  var inicio = document.getElementById('inicio').value;
  var fin = document.getElementById('fin').value;
  var dia = document.getElementById('dia').value;
  var lugar = document.getElementById('lugar').value;
  console.log(profesor);

  if (inicio == cita.hora_inicio && fin == cita.hora_fin && dia == cita.dia && lugar == cita.lugar) {
    swal("¡Administrador!", 'Porfavor efectúe algún cambio', "warning");
  }else {
    if (inicio == "" || fin == "" || dia == "" || lugar == "") {
      swal("¡Espere, administrador!", 'Porfavor termine de escribir los cambios', "warning");
    }else {
      var elementos = "/"+profesor+"/"+inicio+"/"+fin+"/"+dia+"/"+lugar+"/"+"cita"+profesor+inicio+lugar+dia+"/"+cita.codigo_simple;
      swal({
        title: "¿Está seguro administrador?",
        text: "Se va a modificar un horario para el profesor",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          $.get('/principal/a/asesoriaMod'+elementos,function(resp){
            if (resp == "ok") {
              swal({
                title: "¡Se ha modificado el horario!",
                icon: "success",
                dangerMode: true,
              })
              .then((willDelete) => {
                if (willDelete) {
                  var url = sessionStorage.getItem("reg");
                  window.location.replace(url);
                }
              });
            }else if (resp == "") {
              swal({
                title: "¡El horario se cruza con otro!",
                text: "Intente modificar nuevamente",
                icon: "error",
              })
            }else {
              swal({
                title: "¡Intente denuevo!",
                text: "No se puede exceder de dos asesorias por día",
                icon: "error",
              })
            }
          })

        } else {
          swal({
            title: "¡No se ha modificado el horario!",
            icon: "info",
          })
        }
      });
    }
  }


}
