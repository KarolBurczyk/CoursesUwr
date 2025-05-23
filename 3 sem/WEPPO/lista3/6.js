function fibIter() {
    let a = 0;
    let b = 1;

    return {
        next: function () {
            const current = a;
            a = b;
            b = current + b;
            return { 
                value: current, 
                done: false
            };
        }
    };
}

function* fibGen() {
    let a = 0;
    let b = 1;

    while (true) {
        yield a;
        const current = a;
        a = b;
        b = current + b;
    }
}

// var _it = fibIter();
// for ( var _result; _result = _it.next(), !_result.done; ) {
//     console.log( _result.value );
// }

// var _it = fibGen();
// for ( var _result; _result = _it.next(), !_result.done; ) {
//     console.log( _result.value );
// }

// możemy się iterować sposobem for of po generatorze
for ( var i of fibGen() ) {
    console.log( i );
}
