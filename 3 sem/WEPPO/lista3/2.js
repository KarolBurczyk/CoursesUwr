function forEach( a, f ) {
    for (let i = 0; i < a.length - 1; i ++) {
        f(a[i]);
    }
}

function filter( a, f ) {
    new_list = [];
    for (let i = 0; i < a.length - 1; i ++) {
        if (f(a[i])) {
            new_list.push(a[i]);
        }
    }
    return new_list;
}

function map( a, f ) {
    for (let i = 0; i < a.length - 1; i ++) {
        a[i] = f(a[i]);
    }
    return a;
}

var a = [1,2,3,4];

forEach( a, _ => { console.log( _ ); } );
// [1,2,3,4]

console.log(filter( a, _ => _ < 3 ));
// [1,2]

console.log(map( a, _ => _ * 2 ));
// [2,4,6,8]
    