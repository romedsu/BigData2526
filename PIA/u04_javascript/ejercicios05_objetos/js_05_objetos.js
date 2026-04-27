// 1 - USUARIO

// factory
let nuevoUsuario = function (nombre, pass) {
  let obj = {};

  obj.nombre = nombre;
  obj.pass = pass;

  obj.login = function (nombre, pass) {
    return this.nombre === nombre && this.pass === pass;
  };

  return obj;
};

// crear objeto directamente (literal)
let user02 = {
  nombre: "pepe",
  password: "1234",

  login(nombre, password) {
    return this.nombre === nombre && this.password === password;
  },
};

// if(a>b){
//     return true
// }
// else{
//     return false
// }
// return a>b

let user01 = nuevoUsuario("ana", "1234");

// console.log(user01.nombre);
// console.log(user01.login("ana", "1234"));

// console.log(user02.login("pepe", "1234"));

// -------------------------------

// 2 CUADROS

let cuadros = [
  {
    titulo: "Mona Lisa",
    artista: "Leonardo da Vinci",
    fecha: "1503",
  },
  {
    titulo: "La última cena",
    artista: "Leonardo da Vinci",
    fecha: "1495",
  },
  {
    titulo: "Noche estrellada",
    artista: "Vicent van Gogh",
    fecha: "1889",
  },
  {
    titulo: "El grito",
    artista: "Edvard Munch",
    fecha: "1893",
  },
  {
    titulo: "Guernica",
    artista: "Pablo Picasso",
    fecha: "1937",
  },
  {
    titulo: "Las Meninas",
    artista: "Diego Velázquez",
    fecha: "1656",
  },
  {
    titulo: "La creación de Adán",
    artista: "Miguel Ángel",
    fecha: "1512",
  },
];

// cuadros.forEach((obj) => console.log(obj));

// -------------------------------

// 3 CUADROS OBJETOS

// CONSTRUCTOR
let Image = function (titulo, artista, fecha) {
  this.titulo = titulo;
  this.artista = artista;
  this.fecha = fecha;
};

// let cuadro01= new Image('a','aa','11');
// console.log(cuadro01);

// let cuadros1=[...cuadros]
// console.log(cuadros1);

let cuadros1 = cuadros.map(
  (obj) => new Image(obj.titulo, obj.artista, obj.fecha),
);

// console.log(cuadros1);

// FACTORY
let getImage = function (titulo, artista, fecha) {
  let obj = {};

  obj.titulo = titulo;
  obj.artista = artista;
  obj.fecha = fecha;

  return obj;
};

let cuadros2 = cuadros1.map((obj) =>
  getImage(obj.titulo, obj.artista, obj.fecha),
);

// console.log(cuadros2);

// -------------------------------

// 4 ESTUDIANTES | PROFESORES

function sendEmail(from, to, mensaje) {
  console.log("Mensaje enviado");
}

// CLASE
class User {
  constructor(nombre, apellido, email, rol) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.rol = rol;
  }

  addCurso(curso, nivel) {
    if (!this.curso) {
      this.curso = [];
      this.nivel = [];
    }
    this.curso.push(curso);
    this.nivel.push(nivel);
  }

  removeCurso(curso) {
    let i = this.curso.indexOf(curso);
    this.curso.splice(i, 1);
    this.nivel.splice(i, 1);
  }

  editCurso(curso, nivel) {
    let i = this.curso.indexOf(curso);
    this.curso[i] = curso;
    this.nivel[i] = nivel;
  }

  enviarMsg(from, mensaje) {
    if (!this.msjs) {
      this.msjs = [];
    }

    this.msjs.push({ from: from.email, mensaje: mensaje });

    sendEmail(from.email, this.email, mensaje);
  }

  mostrarHistorialMensajes() {
    if (this.msjs) {
      this.msjs.forEach((obj) => console.log(obj));
    }
  }
}

let u = new User("pep", "a", "pepe@email.com", "estudiante");
let u02 = new User("jose", "b", "jose@email.com", "profesor");
let u03 = new User("ana", "c", "ana@email.com", "profesor");

u.addCurso("lengua", "1");
u.addCurso("mates", "2");
u.addCurso("fisica", "3");

u.removeCurso("mates");

u.editCurso("lengua", "0");

// u.enviarMsg(u02, "hola");
// u.enviarMsg(u03, "adios");

// u.mostrarHistorialMensajes();

// console.log(u);

// ------------------------
// 5 USUARIO EXTENDIDO

class UsuarioExtendido extends User {
  get nombreCompleto() {
    // return this.nombre.concat(this.apellido)
    return this.nombre + " " + this.apellido;
  }

  set nombreCompleto(aux) {
    aux = aux.split(" ");
    this.nombre = aux[0];
    this.apellido = aux[1];
  }
}

class Alumno extends UsuarioExtendido {
  constructor(nombre, apellido, email) {
    super(nombre, apellido, email, "Alumno");
  }
}
class Profesor extends UsuarioExtendido {
  constructor(nombre, apellido, email) {
    super(nombre, apellido, email, "Profesor");
  }
}

let es = new UsuarioExtendido("Belarmino", "Domínguez", "belar@email.com");

console.log(es);
es.addCurso("ingles", "3");

es.enviarMsg(u, "hola Belarmino");

// console.log(es);

//  GETTER y SETTER --> no se llaman con ()
// console.log(es.nombreCompleto);

// GETTER --> se llama como propiedad
es.nombreCompleto = "juan perez";

// console.log(es.nombreCompleto);

let profesor01 = new Profesor("zacarias", "campano", "zacas@email.com");

console.log(profesor01);

// ------------------------
// 6 SRI (Sistema de recomendación inteligente)

class SRI {
  constructor(recursos) {
    this.recursos = recursos;
  }

  puntuar(alumno) {
    // let puntuaciones = new Map(this.recursos.map((obj) => {
    let puntuaciones = this.recursos.map((obj) => {
      let puntuacion = 0;

      if (alumno.intereses.includes(obj.tema)) {
        puntuacion += 3;
      }

      if (alumno.nivel == obj.nivel) {
        puntuacion += 3;
      }

      if (obj.tipo == "video") {
        puntuacion += 1;
      }

      if (!alumno.historial.includes(obj.id)) {
        puntuacion += 2;
      } else {
        puntuacion -= 5;
      }

      // alumno.historial.push(obj.tema);

      // return [obj.tema, {...obj,puntuacion:puntuacion}];
      return { ...obj, puntuacion: puntuacion };
    });

    return puntuaciones;
  }

  recomendar(alumno) {
    let puntuaciones = this.puntuar(alumno);
    console.log(puntuaciones);

    // OPCION FOR (version .MAP)
    // let mejorNota=0;
    // let mejor={}

    // for (let[tema,obj] of puntuaciones){
    //   if(obj.puntuacion > mejorNota){
    //     mejor={tema:tema,puntuacion:obj.puntuacion}
    //   }
    // }

    // OPCION FOREACH
    let mejorNota = 0;
    let mejor = {};

    puntuaciones.forEach((obj) => {
      if (obj.puntuacion > mejorNota) {
        mejorNota = obj.puntuacion;
        mejor = { id: obj.id, puntuacion: obj.puntuacion };
      }
    });

    return mejor;
  }
}

let alumnoSRI = {
  nombre: "sara",
  nivel: "4",
  intereses: ["python", "javascript", "mysql"],
  historial: ["javascript", "php"],
};

let recursos01 = [
  { tema: "javascript", tipo: "video", nivel: 2, id: 1 },
  { tema: "python", tipo: "texto", nivel: 1, id: 2 },
  { tema: "mysql", tipo: "video", nivel: 4, id: 3 },
  { tema: "php", tipo: "audio", nivel: 4, id: 3 },
];

let recursosObj = new SRI(recursos01);

console.log(recursosObj.puntuar(alumnoSRI));
console.log(recursosObj.recomendar(alumnoSRI));

//  CONSTRUCTOR recurso

// class recursoSRI{
//   constructor(tema, tipo, nivel, duración, id) {
//       this.tema = tema;
//       this.tipo = tipo;
//       this.nivel = nivel;
//       this.duración = duración;
//       this.id = id;
//     }
//   }

//   let rec01 = new recursoSRI("python", "video", "5", "10", "01");
//   console.log(rec01);
//   let rec02=new recursoSRI({tema:'cine',tipo:'pro',nivle:'5',duración:'larga',id:'01'})
//   console.log(rec02);

// ------------------------------------
// 7 SRI herencia
class SRIupdate extends SRI {
  puntuar(alumno) {
    let puntuaciones = super.puntuar(alumno);

    // puntuaciones.forEach(obj=>{
    //   if (obj.tipo == "video") {
    //     obj.puntuacion += 2;
    //   }
    // })

    // return puntuaciones;

    //  OPCION .MAP
    // let puntuacionesUpdate = puntuaciones.map(obj=>{
    //   if(obj.tipo == "video"){
    //     return {...obj,puntuacion:obj.puntuacion+=2}
    //   }
    //   else{
    //     return {...obj}
    //   }
    // })
    // return puntuacionesUpdate;

    // OPCION 1 LINEA
    let puntuacionesUpdate = puntuaciones.map((obj) =>obj.tipo == "video"? { ...obj, puntuacion: (obj.puntuacion += 2) } : { ...obj });
    return puntuacionesUpdate;
  }
}

let recursosObj2 = new SRIupdate(recursos01);

console.log(recursosObj2.puntuar(alumnoSRI));
