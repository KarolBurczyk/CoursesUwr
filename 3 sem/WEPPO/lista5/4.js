const fs = require('fs');

fs.readFile('tekst.txt', 'utf8', (err, data) => {
  console.log(data);
});
