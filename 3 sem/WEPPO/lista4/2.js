var p = {
    name: 'jan'
}
var q = {
    surname: 'kowalski'
}
Object.setPrototypeOf( p, q );
console.log( p.name );
console.log( p.surname );

function if_proto(p, x) {
    p2 = Object.getPrototypeOf(p);
    if ( p[x] != p2[x]) {
        return false;
    }
    else {
        return true;
    }
}

console.log(if_proto(p, "surname"))
console.log(if_proto(p, "name"))