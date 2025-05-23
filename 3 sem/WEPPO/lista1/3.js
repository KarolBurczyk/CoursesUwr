function czy_pierwsza(x) {
    for (let i = 2; i < x/2 + 1; i++)   {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

for (let k = 2; k <= 100000; k++)   {
    if (czy_pierwsza(k) == true)    {
        console.log(k);
    }
}