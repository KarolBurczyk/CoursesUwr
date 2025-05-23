function fibIter() {
    let a = 1;
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
    let a = 1;
    let b = 1;

    while (true) {
        yield a;
        const current = a;
        a = b;
        b = current + b;
    }
}

function* take(it, top) {
    let i = 0
    while (i < top) {
        yield it.next().value;
        i++;
    }
}

for (let num of take( fibIter(), 10 ) ) {
    console.log(num);
}

console.log();

for (let num of take( fibGen(), 10 ) ) {
    console.log(num);
}
