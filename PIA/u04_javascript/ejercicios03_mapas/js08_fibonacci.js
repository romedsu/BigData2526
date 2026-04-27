const fibonacci = (n) => {
  let total;
  let aux = 1;
  let aux2 = 1;
  let aux3 = 2;
  let secuencia = [];

  for (let i = 0; i < n; i++) {
    total = aux + aux2 + aux3;
    secuencia.push(total);

    aux = aux2;
    aux2 = aux3;
    aux3 = total;
  }

  return secuencia;
};


console.log(fibonacci(5));

