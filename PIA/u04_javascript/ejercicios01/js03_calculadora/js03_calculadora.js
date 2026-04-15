let n1, op, n2, resultado;

n1= Number(window.prompt("Introduce 1er nº:"));
if (Number.isNaN(n1)){
    console.log('No has introducido un nº');
}

op= window.prompt("Introduce la operación que deseas realizar: (+, -, *, /)");

n2= Number(window.prompt("Introduce 2º nº:"));
if (Number.isNaN(n2)){
    console.log('No has introducido un nº');
}
switch (op){
    case "+":{
        resultado=n1 + n2;
        break;
    }
    case "-":{
        resultado=n1 - n2;
        break;
    }
    case "*":{
        resultado=n1 * n2;
        break;
    }
    case "/":{
        resultado=n1 / n2;
        break;
    }
    default:{
        alert('Opción no valida');
        break;
    }
}

console.log(resultado);

alert(resultado);

