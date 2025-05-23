sub10 = require('./modules_require');

function add10(x) {
    return x + 10;
}

console.log(sub10(11));

module.exports = add10;

// moduly nie moga korzystac z siebie nawzajem, bo powstaje niskonczona rekurencja, gdy odwoluja sie do siebie nawzajem 

