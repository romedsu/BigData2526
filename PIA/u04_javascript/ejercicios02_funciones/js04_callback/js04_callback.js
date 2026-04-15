let n1=10;
let n2=3;

function ejecuta (callback,a,b){
    return callback(a,b);
}

const ejecutaF =(callback,a,b) => callback(a,b);

const sumaF = (a,b) => Number.isInteger(a) && Number.isInteger(b)? a+b : NaN;

console.log(ejecutaF(sumaF,n1,n2));




