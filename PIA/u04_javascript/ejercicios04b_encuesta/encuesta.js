datos = [
        { nombre: "Alberto", 
        edad: 44, 
        educacion: 4, 
        finanzas: 8, 
        sanidad: 6, 
        transporte: 9 },

        { nombre: "Elena", 
        edad: 70, 
        educacion: 1, 
        finanzas: 8, 
        sanidad: 9, 
        transporte: 8 },

        { nombre: "Carla", 
        edad: 40, 
        educacion: 6, 
        finanzas: 7, 
        sanidad: 8, 
        transporte: 6 },

        { nombre: "Pepe", 
        edad: 40, 
        educacion: 10, 
        finanzas: 7, 
        sanidad: 8, 
        transporte: 5 },
];



// 1 --> MAYORES 50
let mas50 = datos.filter(obj=> obj.edad > 50 && obj.sanidad >5)


// 2 --> EDUCACION y SANIDAD
let educSan = datos.filter(obj => obj.educacion > 5 && obj.sanidad >5)

educSan.forEach(obj=>console.log(obj));


// 3 --> EDAD
let edades=datos.map(obj =>obj.edad);

let edadesSet=new Set(edades)
let edadesArray = [...edadesSet]

console.log(edades);
console.log(edadesSet);
console.log(edadesArray);

console.log(Math.max(...edadesArray));

console.log(Math.min(...edadesArray));


// 4 --> MEDIA VALORACIONES (ordenado)
let valoraciones = new Map(datos.map(obj=>{
        let media = (obj.educacion + obj.finanzas + obj.sanidad + obj.transporte) /4

        return [obj.nombre, media]
}))

console.log(valoraciones);

valoraciones=[...valoraciones]

valoraciones.sort((a,b)=>a[1]-b[1])

console.log(valoraciones);



// 5 NUEVA PROPIEDAD

// let datosUpdate = datos.map(obj=>({
//      ...obj,
//      conforme:((obj.educacion + obj.finanzas + obj.sanidad + obj.transporte) /4 )>=7
// }))

let datosUpdate = datos.map(obj=>({
     ...obj,
     conforme:((obj.educacion + obj.finanzas + obj.sanidad + obj.transporte) /4 )>=7
}))

console.log(datosUpdate);
