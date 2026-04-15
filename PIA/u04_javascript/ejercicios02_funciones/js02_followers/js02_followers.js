const followers = new Set();
let opcion, aux;

// do{
//     opcion=window.prompt("- Añadir un seguidor (1)\n- Eliminar un seguidor (2)\n- Mostrar todos los seguidores (3)\n- Comprobar si una “persona” entre los seguidores (4)\n - Salir del programa (quit) ")

//     switch (opcion){
//         case '1':{
//             aux=window.prompt("Nombre nuevo seguidor:");
//             nuevo(aux);
//             break;
//         }
//         case '2':{
//             aux=window.prompt("Nombre seguidor que desear eliminar:");
//             borrar(aux);
//             break;
//         }
//         case '3':{
//             mostrar(followers);
//         }
//     }

// }while(opcion);


function nuevo() {
    aux = window.prompt("Nombre NUEVO seguidor:");
    followers.add(aux);

     document.getElementById('info').innerHTML('nuevo')
    return followers;
}

function borrar() {
    aux = window.prompt("Nombre seguidor que deseas ELIMINAR:");

    if(followers.has(aux)){
        followers.delete(aux);
    }
    else{
        alert(`${aux} NO es tu seguidor`)
    }

    return followers;
}

function mostrar() {
    for (let elem of followers) {
        alert(elem);
    }
}

function comprobar(){
    aux = window.prompt("Nombre seguidor que desear COMPROBAR:");
    if (followers.has(aux)){
        alert(`${aux} es tu seguidor`);
    }
    else{
        alert(`${aux} NO es tu seguidor`);
    }
}

function salir(){
    alert('FINALIZADO');
}


document.getElementById("info").innerHTML='<p>hola</p>';


// document.write("<p>Adios</p>")