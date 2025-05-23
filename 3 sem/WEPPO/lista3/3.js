function createFs(n) {
    var fs = [];
    for (let i = 0; i < n; i++) {
        fs[i] =
            function () {
                return i;
            };
    };
    return fs;
}
var myfs = createFs(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());
console.log()
//zamiana na let sprawia, że funkcje przechowywane w fs nie będą miały odnośnika do jednej i tej samej zmiennej,
//tylko każda będzie wewnętrznie przechowywać własną 

function createFs(n) {
    var fs = [];
    var loop = function loop(i) {
        fs[i] = 
            function () {
                return i;
            };
    };
    for (var i = 0; i < n; i++) {
        loop(i);
    };
    return fs;
}
var myfs = createFs(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());