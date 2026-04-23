// ns=[1,1,1,1,1,1,1,1,]

// OP MAP (el array no puede estar vacío)
// let aleatorios =(array)=>{
//         let lleno = array.map(() => Math.trunc((Math.random()*100)+1);
//         return lleno;
//     }

let aleatorios = () => {
  let array = new Array(10);
  for (let i = 0; i < array.length; i++) {
    array[i] = Math.trunc(Math.random() * 100 + 1);
  }

  //ordena
  // (sin la callback como argumneto, los valores de un nº (1,2,etc) no los ordena bien)
  array.sort((a, b) => {
    if (a % 10 == 0) {
      return -1;
    } else if (b % 10 == 0) {
      return 1;
    } else {
      return a - b;
    }
  });

  return array;
};

console.log(aleatorios());
