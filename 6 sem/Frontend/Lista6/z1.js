//Przed:

console.log(capitalize("alice"));

const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};  

// Po:

console.log(capitalize("alice"));

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
};