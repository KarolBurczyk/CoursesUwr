function rek(n) {
    if (n <= 2) {
        return 1;
    }
    else {
        return rek(n - 1) + rek(n - 2);
    }
}

function fib(n) {
    if (n <= 2) {
        return 1;
    }
    else {
        if (!fib.cachedResults[n]) {
            result = fib(n - 1) + fib(n - 2);
            fib.cachedResults[n] = result;
        }
    
        return fib.cachedResults[n];
    }
}

fib.cachedResults = {};

console.time();
console.log(fib(40));
console.timeEnd();
console.time();
console.log(rek(40));
console.timeEnd();
console.time();
console.log(fib(40));
console.timeEnd();
console.time();
console.log(rek(40));
console.timeEnd();