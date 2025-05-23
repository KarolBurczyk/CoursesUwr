type FibCache = {
    [key: number]: number;
}

function fib(n : number) : number{
    if (n <= 2) {
        return 1;
    }
    else {
        if (!fib.cachedResults[n]) {
            let result : number = fib(n - 1) + fib(n - 2);
            fib.cachedResults[n] = result;
        }
    
        return fib.cachedResults[n];
    }
}

fib.cachedResults = {} as FibCache;

console.time();
console.log(fib(50));
console.timeEnd();