const dados = (n) => {
  let tiradas = new Map();
  let maximo = 0;

  for (let i = 1; i <= n; i++) {
    let dado1 = Math.trunc(Math.random() * 6 + 1);
    let dado2 = Math.trunc(Math.random() * 6 + 1);

    tiradas.set(`dado1 - i[${i}]`, dado1).set(`dado2 - i[${i}]`, dado2);
  }

  for (value of tiradas.values()) {
    if (value > maximo) {
      maximo = value;
    }
  }

  // en un objeto map, el .values devuelve un iterador (no un array) con los valores
  // con el uso del spread (...) en el iterador --> lo desfragmenta en valores individuales, y Math.max() saca el máximo.

  // let maximo2 = Math.max(...tiradas.values());

  return maximo;
};

console.log(dados(5));
