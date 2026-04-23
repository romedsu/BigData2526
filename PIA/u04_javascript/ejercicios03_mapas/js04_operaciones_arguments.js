// rest (empaqueta (array))
// const operaciones= (...args)=>{

//  ***ARGUMENTS --> NO FUNCIONA con FN FLECHA **

function operaciones() {
  let suma = 0;
  // let array = [...arguments];

  const resultado = new Map();

  for (let i = 0; i < arguments.length; i++) {
    suma += arguments[i];
  }
  console.log(suma);

  resultado.set("suma", suma);

  resultado.set("media", suma / arguments.length);

  resultado.set(
    "multiplicacion",
    arguments[0] * arguments[arguments.length - 1],
  );

  resultado.set("division", arguments[1] / arguments[arguments.length - 2]);

  return resultado;
}

let entrada = [2, 5, 7, 8];
// console.log(entrada[entrada.length-3]);

// spead (desempaqueta)
// console.log(operaciones(...entrada));

// console.log(operaciones(8, 8, 7, 8, 8));
console.log(operaciones(8, 1, 9, 5));
// console.log(operaciones(8, 8, 8, 8));
