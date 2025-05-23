function forEach<T>( a: T[], f: (t: T) => any ): any{
    for (let i : number = 0; i < a.length - 1; i ++) {
        f(a[i]);
    }
}

function filter<T>( a: T[], f: (t: T) => boolean ): T[] {
    let new_list : T[]= [];
    for (let i : number = 0; i < a.length - 1; i ++) {
        if (f(a[i])) {
            new_list.push(a[i]);
        }
    }
    return new_list;
}

function map<T>( a: T[], f: (t: T) => T ): T[] {
    for (let i : number = 0; i < a.length - 1; i ++) {
        a[i] = f(a[i]);
    }
    return a;
}

var a : number[] = [1,2,3,4];

forEach( a, _ => { console.log( _ ); } );

console.log(filter( a, _ => _ < 3 ));

console.log(map( a, _ => _ * 2 ));
    