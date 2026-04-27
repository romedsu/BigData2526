let productos = [
  {
    nombre: "pc",
    precio: 1500.0,
    categoria: "equipos",
    stock: 3,
  },
  {
    nombre: "monitor",
    precio: 175.0,
    categoria: "perifericos",
    stock: 2,
  },
  {
    nombre: "GPU",
    precio: 950.0,
    categoria: "componentes",
    stock: 0,
  },
  {
    nombre: "SSD",
    precio: 125.0,
    categoria: "componentes",
    stock: 5,
  },
];

// 1 ORDENAR

const ordenar = (inv) => {
  let filtrados = inv.filter((obj) => {
    return obj.stock > 0;
  });

  //   function ordenar (a,b){
  //     if(a.precio > b.precio){
  //         return 1
  //     }
  //     else if (a.precio < b.precio){
  //         return -1
  //     }
  //     else{
  //         return 0
  //     }
  //   }

  // en el cuerpo de la función accedo a la propiedades del objeto que se pasa por parametro (a,b)
  let ordenados = filtrados.sort((a, b) => a.precio - b.precio);

  //  ordenados.forEach((a) => {
  //     console.log(a.nombre);
  //   });

  let nombres = ordenados.map((obj) => {
    return obj.nombre;
  });

  return nombres;
};

let nombres = ordenar(productos);

console.log(nombres);

// ------------<>------------

// 2 DESCUENTO 10%
console.log("2 -- DESCUENTO ---");

const descuento = (productos) => {
  // let descuentos= productos.map(obj=>{
  //    return {...obj,
  //           precio:obj.precio * 1.10,
  //           prueba:'p5'}
  // });

  let descuentos = productos.map((obj) => ({
    ...obj,
    precio: obj.precio * 1.1,
  }));

  return descuentos;
};

console.log(descuento(productos));

// ------------<>------------

// 3 MOSTRAR categorias
console.log("3 -- MOSTRAR ---");

const mostrar = (productos) => {
  let muestra = new Set();

  productos.forEach((obj) => muestra.add(obj.categoria));

  // for(obj of productos){
  //     muestra.add(obj.categoria);
  // }

  let array = [...muestra];

  array.sort();

  return array;
};

console.log(mostrar(productos));

// ------------<>------------

// 4 AÑADIR
console.log("4 -- AÑADIR ---");

const add = (productos, n, p, c, s) => {
  let copy = [...productos];

  // copy.push({
  //   'nombre':n,
  //   'precio':p,
  //   'categoria':c,
  //   'stock':s
  // })

  let nuevo = { nombre: n, precio: p, categoria: c, stock: s };

  //en un nuevo array, copia los originales y añade el nuevo
  copy = [...productos, nuevo];

  return copy;
};

console.log(add(productos, "teclado", 75.0, "perifericos", 3));

// ------------<>------------

// 5 STOCK (map)
console.log("5 -- STOCK ---");

// const stock= (productos=>{

// tupla (nuevo array)
// let productosArray = productos.map(obj=>[obj.nombre,obj])

// // nuevo map (de array -->  map)
// let productosMap = new Map(productosArray);

// en una linea
// let productosMap = new Map(productos.map(obj=>[obj.nombre,obj]));

// console.log(productosArray);
// console.log(productosMap);
// console.log(productosMap.get('pc'));

// nuevo array (de map --> array)
// let productosArray =[...productosMap]

// console.log(productosArray);

// let stockFilter = productosMap.map(obj=>{
//   if (obj[1].stock >0){
//     return true;
//   }
//   else{
//     return false
//   }
// });

// let stockFilter = productosArray.filter(obj=>{
//   return obj[1].stock >0
// });

// stockFilter.forEach(obj=>{
//   console.log(obj[0]);
//   console.log(obj[1].precio);
// })
// foreach(valor,clave) --> clg ¿? igual solo si es un mapa

// });

// --- ---

const stock = (productos) => {
  let stockFilter = productos.filter((obj) => {
    return obj.stock > 0;
  });

  let stockMap = new Map(stockFilter.map((obj) => [obj.nombre, obj]));

  return stockMap;
};

let stockMap = stock(productos);

// ------------<>------------

// 6 TRANSFORMAR

// let array_objetos =[...nuevo_mapa].map([nombre,objeto])

// let arrayStock =[...stockMap]

// let arrayStock =[...stockMap].map(obj=>[obj[1].nombre,obj[1].precio])

let arrayStock = [...stockMap].map(([key, obj]) => {
  return {
    nombre: key,
    precio: obj.precio,
  };
});

console.log(arrayStock);
