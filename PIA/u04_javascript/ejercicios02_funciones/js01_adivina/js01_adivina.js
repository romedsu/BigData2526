let n= Math.trunc(Math.random(0,1)*100);

console.log(n);

function jugar(n){
    let n2=Number(window.prompt('Introduce un nº:'))
    let i=4
    for(i; i>0;i--){
        if (n2 > n){
            n2= Number(window.prompt(`MENOR\nIntroduce otro nº\nTe quedan ${i} intentos`))
        }
        else if (n2 < n){
            n2= Number(window.prompt(`MAYOR\nIntroduce otro nº\nTe quedan ${i} intentos`))
        }
        else{
            alert('HAS ACERTADO');
            break;
        }
    }
    
    if(i==0){
        alert('SE TE HAN ACABADO LOS INTENTOS\nHAS PERDIDO')
    }
}


