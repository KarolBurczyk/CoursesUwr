function foo(n : number) : number {
    return n * n;
}

function foo1(n : number) : number {
    return n + 10;
}

function foo2(n : number) : number {
    return n / 2;
}

function foo3(n : number) : number {
    return n * 10;
}

export default foo;
export {foo1, foo2, foo3};