let n1, op, n2, resultado, e1, e2;

do {
    e1 = window.prompt("Introduce 1er nº: \n Q --> SALIR");
    n1 = Number(e1);
    
    op = window.prompt("Operación (+, -, *, /): \n Q --> SALIR");
    
    e2 = window.prompt("Introduce 2º nº: \n Q --> SALIR");
    n2 = Number(e2);
    

    switch (op){
    case "+":
        resultado=n1 + n2;
        break;
    case "-":
        resultado=n1 - n2;
        break;
    case "*":
        resultado=n1 * n2;
        break;
    case "/":
        resultado=n1 / n2;
        break;
}

    alert("Resultado: " + resultado);

} while (e1 != "Q" && e2 != "Q" && op != "Q");

alert("CALCULADORA FINALIZADA")


