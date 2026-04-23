const palabras = ['hola', 'Ç*h#', 'adios', 'jamon', '!$%', 'paella','cho[]rizo','fabada'];

const abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
];

// console.log(palabras.includes('hola'));
// let a='hola'
// console.log(a.split(''))

const excluir = (args, abcd) => {
    let excluidas;

    excluidas = args.filter((palabra)=>{
        for (letra of palabra){
            if(!abcd.includes(letra)){
                return true;
            }
        }
    })
   

    return excluidas;

}

console.log(excluir(palabras, abecedario));