for (let i = 1; i <= 100000; i++) {
    let x = i.toString();
    let czy = 1;
    let suma = 0;
    for (let j = 0; j < x.length; j++)    {
        suma += Number(x[j]);
        if (i % Number(x[j]) != 0)  {
            czy = 0
            break;
        }
    }
    
    if (czy == 1)   {
        if (i % suma == 0)  {
            console.log(i);
        }
    }
}
