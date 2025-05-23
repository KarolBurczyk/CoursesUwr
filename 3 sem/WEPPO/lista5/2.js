var stdin = process.openStdin();

console.log("Podaj imie: ")

stdin.addListener("data", function(d) {
    console.log("Witaj " + 
        d.toString());
    stdin.pause();
});
