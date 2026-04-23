const numeros = [56, 33, 6, 99, 86, 24];

const numeros2 = [];
for (let i = 0; i < 10; i++) {
  numeros2.push(Math.trunc(Math.random() * 200));
}
console.log(numeros2);

const incrementar = (args) => {
  let nuevos = args.map((n) => {
    // if(n<100){
    //     return n+10;
    // }
    // else{
    //     return n;
    // }

    return n < 100 ? n + 10 : n;
  });
  return nuevos;
};

console.log(incrementar(numeros2));

function incrementar2(nums) {
  return nums.filter((n) => n < 100).map((n) => (n += 10));
}

console.log(incrementar2(numeros2));
