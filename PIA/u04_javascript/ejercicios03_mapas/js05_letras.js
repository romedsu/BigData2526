let p1 = "pepe";
let p2 = "pepep";

const analizar = (a, b) => {
  let letras = new Map();

  const args1 = [...a];
  const args2 = [...b];
  console.log(args2);

  let letras1 = new Map();
  let letras2 = new Map();

  args1.forEach((letra) => {
    if (!letras1.has(letra)) {
      letras1.set(letra, 1);
    } else {
      let aux = letras1.get(letra);
      aux++;
      letras1.set(letra, aux);
    }
  });

  args2.forEach((letra) => {
    if (!letras2.has(letra)) {
      letras2.set(letra, 1);
    } else {
      let aux = letras2.get(letra);
      aux++;
      letras2.set(letra, aux);
    }
  });

  if (letras1.size !== letras2.size) {
    return false;
  }

  for (let [key, value] of letras1) {
    if (letras2.has(key)) {
      if (value !== letras2.get(key)) {
        return false;
      }
    }
    return true;
  }

  return false;
};

console.log(analizar(p1, p2));
