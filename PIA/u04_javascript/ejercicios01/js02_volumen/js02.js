let ancho = Number(window.prompt("ancho:"));
let alto = Number(window.prompt("alto:"));
let largo = Number(window.prompt("largo:"));

console.log(typeof ancho);

if (typeof ancho !== 'number' && alto !== 'number' && largo !== 'number'){
    alert('Tipo de valores incorrectos')
}
else{
    let volumen= ancho * alto * largo;
    alert(`Volumen de la caja: ${volumen}`);
    
}
