// OPCION ARRAYS

// let peliculas=[], calificaciones=[], pelicula,calificacion, decision;

// do{
//     pelicula=window.prompt("Nombre de la película:");

//     peliculas.push(pelicula);

//     calificacion=Number(window.prompt("Calificación:"));

//     calificaciones.push(calificacion)

//     decision= window.confirm('¿Nueva película?')
//     console.log(decision)

// }while(decision == true)

// for(let i =0; i< peliculas.length; i++ ){
//     if (calificaciones[i] < 7){
//         console.log(`${peliculas[i]} ( ${calificaciones[i]} )`)
//     }
// }

// for(let i =0; i< peliculas.length; i++ ){
//     if (calificaciones[i] >= 7){
//         console.log(`${peliculas[i]} ( ${calificaciones[i]} )`)
//     }
// }

// --------------------
// OPCION OBJETOS

let peliculas = [],
  calificaciones = [],
  pelicula,
  calificacion,
  decision;

do {
  pelicula = window.prompt("Nombre de la película:");

  calificacion = Number(window.prompt("Calificación:"));

  peliculas.push({
    pelicula: pelicula,
    calificacion: calificacion,
  });

  decision = window.confirm("¿Nueva película?");
  console.log(decision);
} while (decision == true);

// let peliculas= [
//   {
//     "pelicula": "Inception",
//     "calificacion": 9
//   },
//   {
//     "pelicula": "Titanic",
//     "calificacion": 8
//   },
//   {
//     "pelicula": "Interstellar",
//     "calificacion": 9.5
//   }
// ]

for (let i = 0; i < peliculas.length; i++) {
  if (peliculas[i].calificacion < 7) {
    console.log(`${peliculas[i].pelicula} ( ${peliculas[i].calificacion} )`);
  }
}
for (let i = 0; i < peliculas.length; i++) {
  if (peliculas[i].calificacion >= 7) {
    console.log(`${peliculas[i].pelicula} ( ${peliculas[i].calificacion} )`);
  }
}

for (let p of peliculas) {
  console.log(p.calificacion);
}
for (let p in peliculas) {
  console.log(peliculas[p].calificacion);
}
