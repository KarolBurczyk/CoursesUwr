function sum(...arguments) {
    let args = Array.from(arguments);
    let sum = args.reduce(function(a, b){
        return a + b;
    });
    return sum;
}

console.log(sum(1,2,3));
// 6

console.log(sum(1,2,3,4,5));
// 15