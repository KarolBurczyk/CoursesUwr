function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
};

function capitalizeSentence (str) {
    return str.split(" ").map(word => capitalize(word)).join(" ");
};

console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));