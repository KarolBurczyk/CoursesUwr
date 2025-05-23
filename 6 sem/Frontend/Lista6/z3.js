// Używamy zbioru zamiast tablicy

// const ids = [];

// const generateId = () => {
//   let id = 0;

//   do {
//     id++;
//   } while (ids.includes(id));

//   ids.push(id);
//   return id;
// };

const ids = new Set();

const generateId = () => {
    let id = 0;
    do {
        id++;
    } while (ids.has(id));

    ids.add(id);
    return id;
};

console.time("generateId");
for (let i = 0; i < 3000; i++) {
    generateId();
}
console.timeEnd("generateId");
