let estilos=['Jazz','Blues'];

estilos.push('Rock');

estilos[1]='Clásica';

// eliminar y devolver 1er valor
console.log(estilos.shift())

// insertar 1ª posición
estilos.unshift('Rap','Reggae');

console.log(estilos);