function createGenerator(n) {
    var state = 0;
    return {
        next: function () {
            return {
                value: state,
                done: state++ >= n
            };
        }
    };
}

var foo10 = {
    [Symbol.iterator]: function () {
        return createGenerator(10);
    }
};

var foo20 = {
    [Symbol.iterator]: function () {
        return createGenerator(20);
    }
};

for (var f of foo20) {
    console.log(f);
}
    