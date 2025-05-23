var stdin = process.openStdin();

var liczba = Math.floor(Math.random() * 100);
console.log("Podaj liczbe: ");

stdin.addListener("data", function(d) {
    if (Number(d.toString()) == liczba) {
        console.log('to jest właśnie ta liczba');
        stdin.pause();
    }
    else if (Number(d.toString()) > liczba) {
        console.log('moja liczba jest mniejsza');
    }
    else {
        console.log('moja liczba jest wieksza');
    }
});
