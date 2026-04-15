contactos=[
    {
        "nombre":'ana',
        "telefono":"611111111",
        "email":'ana@email.com'
    },
    {
        "nombre":'belarmino',
        "telefono":"62222222",
        "email":'belarmino@email.com'
    },
    {
        "nombre":'celia',
        "telefono":"63333333",
        "email":'celia@email.com'
    }
]

let opcion;

do{
    opcion=window.prompt("ACCIÓN:\n -mostrar el primer contacto (primero) \n- mostrar el último contacto (last) \n- mostrar todos los contactos (todos) \n- añadir un nuevo contacto (nuevo) \n- salir del prog (quit)");

    switch(opcion){
        case "primero":{
            console.log(contactos[0]);
            break;
        }
        case "last":{
            console.log(contactos[(contactos.length)-1]);
            break;
        }
        case "todos":{
            console.log(contactos);
            break;
        }
        case "nuevo":{
            let nombre=window.prompt("Nombre nuevo contacto:");
            let telefono=window.prompt("Teléfono nuevo contacto:");
            let email=window.prompt("email nuevo contacto:");

            contactos.push({
                            "nombre":nombre,
                            "telefono":telefono,
                            "email":email
            })
            break;
        }
        case "quit":
            break;

        default:
            console.log("Operación NO VÁLIDA");
    }

}while(opcion != 'quit')

