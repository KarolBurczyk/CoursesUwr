function iter(n) {
    let a = 1;
    let b = 1;
    if (n == 1) {
        return 1;
    }
    else {
        while (n - 2 > 0) {
            let c = a;
            a = b;
            b = a + c;
            n = n - 1;
        }
        return b;
    }
}

function rek(n) {
    if (n <= 2) {
        return 1;
    }
    else {
        return rek(n - 1) + rek(n - 2);
    }
}

console.time();
console.log(iter(100))
console.log("Czas iteracyjny:")
console.timeEnd();

// console.time();
// console.log(rek(40))
// console.log("Czas rekurencyjny:")
// console.timeEnd();
