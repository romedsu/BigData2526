let p1 ='casa';
let p2 = 'casat';

function comparar(p1,p2){
    let set1=new Set(p1);
    let set2=new Set(p2);

    let flag=true;

    set1.forEach(letra=> flag = flag && set2.has(letra));

    set2.forEach(letra => flag= flag && set1.has(letra) );

    return flag

}

console.log(comparar(p1,p2));