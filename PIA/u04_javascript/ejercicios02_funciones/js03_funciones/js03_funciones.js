console.time("tiempo inicio");

let resultado;

let a, b;

a = Number(window.prompt('Introduce 1er operador'));
b = Number(window.prompt('Introduce 2º operador'));

let suma = function (a, b) {
    if (Number.isInteger(a) && Number.isInteger(b)) {
        resultado = a + b;
        document.getElementById('info').innerHTML = `${a} + ${b} = ${resultado}`;
        return resultado;
    }
    else {
        document.getElementById('info').innerHTML = `${NaN}`;
        return NaN;
    }
}

let resta = function (a, b) {
    if (Number.isInteger(a) && Number.isInteger(b)) {
        resultado = a - b;
        document.getElementById('info').innerHTML = `${a} - ${b} = ${resultado}`;
        return resultado;
    }
    else {
        document.getElementById('info').innerHTML = `${NaN}`;
        return NaN;
    }
}
let multiplo = function (a, b) {
    if (Number.isInteger(a) && Number.isInteger(b)) {
        resultado = a * b;
        document.getElementById('info').innerHTML = `${a} * ${b} = ${resultado}`;
        return resultado;
    }
    else {
        document.getElementById('info').innerHTML = `${NaN}`;
        return NaN;
    }
}
let division = function (a, b) {
    if (Number.isInteger(a) && Number.isInteger(b)) {
        resultado = a / b;
        document.getElementById('info').innerHTML = `${a} / ${b} = ${resultado}`;
        return resultado;
    }
    else {
        document.getElementById('info').innerHTML = `${NaN}`;
        return NaN;
    }
}

// VERSION FLECHA
let sumaF = (a,b) => Number.isInteger(a) && Number.isInteger(b)? a+b : NaN;

let restaF = (a,b) =>Number.isInteger(a) && Number.isInteger(b)? a-b : NaN;

let multiploF = (a,b) => Number.isInteger(a) && Number.isInteger(b)? a*b : NaN;

let divisionF = (a,b) =>Number.isInteger(a) && Number.isInteger(b)? a/b : NaN;




console.timeEnd("tiempo inicio");