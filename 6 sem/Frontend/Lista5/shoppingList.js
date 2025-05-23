/**
 * @typedef {Object} Product
 * @property {number} id - Unikalny identyfikator produktu
 * @property {string} name - Nazwa produktu
 * @property {number} quantity - Liczba sztuk do zakupienia
 * @property {Date} dueDate - Data, do której produkt powinien być zakupiony
 * @property {boolean} purchased - Status informujący, czy produkt został zakupiony
 * @property {number} [pricePerUnit] - Cena za sztukę
 */

/** @type {Product[]} */
let shoppingList = [];

/**
 * Dodaje nowy produkt do listy zakupów
 * @param {string} name 
 * @param {number} quantity 
 * @param {string} dueDateString 
 */
function addProduct(name, quantity, dueDateString) {
    const product = {
        id: Math.floor(Math.random() * 1000000),
        name: name,
        quantity: quantity,
        dueDate: new Date(dueDateString),
        purchased: false
    };
    shoppingList.push(product);
}

/**
 * Usuwa produkt z listy na podstawie id
 * @param {number} id 
 */
function removeProduct(id) {
    shoppingList = shoppingList.filter(product => product.id !== id);
}

/**
 * Edytuje nazwę produktu na podstawie id
 * @param {number} id 
 * @param {string} newName 
 */
function editProductName(id, newName) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.name = newName;
}

/**
 * Edytuje liczbę sztuk produktu na podstawie id
 * @param {number} id 
 * @param {number} newQuantity 
 */
function editProductQuantity(id, newQuantity) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.quantity = newQuantity;
}

/**
 * Edytuje datę zakupu produktu na podstawie id
 * @param {number} id 
 * @param {string} newDueDateString 
 */
function editProductDueDate(id, newDueDateString) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.dueDate = new Date(newDueDateString);
}

/**
 * Zmienia status produktu na zakupiony
 * @param {number} id 
 * @param {boolean} purchased 
 */
function editProductStatus(id, purchased) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.purchased = purchased;
}

/**
 * Przesuwa produkt w górę listy
 * @param {number} id 
 */
function moveProductUp(id) {
    const index = shoppingList.findIndex(product => product.id === id);
    if (index > 0) {
        [shoppingList[index], shoppingList[index - 1]] = [shoppingList[index - 1], shoppingList[index]];
    }
}

/**
 * Przesuwa produkt w dół listy
 * @param {number} id 
 */
function moveProductDown(id) {
    const index = shoppingList.findIndex(product => product.id === id);
    if (index !== -1 && index < shoppingList.length - 1) {
        [shoppingList[index], shoppingList[index + 1]] = [shoppingList[index + 1], shoppingList[index]];
    }
}

/**
 * Zamienia miejscami dwa produkty na podstawie ich id
 * @param {number} id1 
 * @param {number} id2 
 */
function swapProducts(id1, id2) {
    const index1 = shoppingList.findIndex(product => product.id === id1);
    const index2 = shoppingList.findIndex(product => product.id === id2);
    if (index1 !== index2) {
        [shoppingList[index1], shoppingList[index2]] = [shoppingList[index2], shoppingList[index1]];
    }
}

/**
 * Zwraca listę produktów do zakupienia dziś
 * @returns {Product[]}
 */
function getProductsToBuyToday() {
    const today = new Date().toDateString();
    return shoppingList.filter(product => !product.purchased && product.dueDate.toDateString() === today);
}

/**
 * Ustawia cenę dla zakupionego produktu
 * @param {number} id 
 * @param {number} pricePerUnit 
 */
function setProductPrice(id, pricePerUnit) {
    const product = shoppingList.find(product => product.id === id);
    if (product && product.purchased) product.pricePerUnit = pricePerUnit;
}

/**
 * Oblicza koszt zakupów danego dnia
 * @param {string} dateString 
 * @returns {{totalCost: number, missingPrices: string[]}}
 */
function calculateShoppingCost(dateString) {
    const date = new Date(dateString).toDateString();
    let totalCost = 0;
    let missingPrices = [];

    shoppingList.forEach(product => {
        if (product.purchased && product.dueDate.toDateString() === date) {
            if (product.pricePerUnit !== undefined) {
                totalCost += product.pricePerUnit * product.quantity;
            } else {
                missingPrices.push(product.name);
            }
        }
    });
    
    return { totalCost, missingPrices };
}

/**
 * Masowe formatowanie listy zakupów
 * @param {number[]} ids - Lista id produktów do zmodyfikowania
 * @param {(product: Product) => void} modifyFunction - Funkcja modyfikująca produkt
 */
function bulkModifyProducts(ids, modifyFunction) {
    shoppingList = shoppingList.map(product => {
        if (ids.includes(product.id)) {
            modifyFunction(product);
        }
        return product;
    });
}

function runTests() {
    console.log("Running tests...");

    shoppingList = [];
    addProduct("Milk", 2, "2025-04-02");
    console.assert(shoppingList.length === 1, "addProduct failed");

    const milkId = shoppingList[0].id;
    removeProduct(milkId);
    console.assert(shoppingList.length === 0, "removeProduct failed");

    addProduct("Bread", 1, "2025-04-02");
    const breadId = shoppingList[0].id;
    editProductName(breadId, "Whole Grain Bread");
    console.assert(shoppingList[0].name === "Whole Grain Bread", "editProductName failed");

    editProductQuantity(breadId, 3);
    console.assert(shoppingList[0].quantity === 3, "editProductQuantity failed");

    editProductDueDate(breadId, "2025-04-03");
    console.assert(shoppingList[0].dueDate.toDateString() === new Date("2025-04-03").toDateString(), "editProductDueDate failed");

    editProductStatus(breadId, true);
    console.assert(shoppingList[0].purchased === true, "editProductStatus failed");

    shoppingList = [];
    addProduct("Apples", 5, "2025-04-02");
    addProduct("Bananas", 3, "2025-04-02");
    const appleId = shoppingList[0].id;
    const bananaId = shoppingList[1].id;

    moveProductUp(bananaId);
    console.assert(shoppingList[0].id === bananaId, "moveProductUp failed");

    moveProductDown(bananaId);
    console.assert(shoppingList[1].id === bananaId, "moveProductDown failed");

    swapProducts(appleId, bananaId);
    console.assert(shoppingList[1].id === appleId, "swapProducts failed");
    console.assert(shoppingList[0].id === bananaId, "swapProducts failed");

    console.log(shoppingList)

    shoppingList = [];
    addProduct("Oranges", 4, new Date().toISOString());
    console.assert(getProductsToBuyToday().length === 1, "getProductsToBuyToday failed");

    editProductStatus(shoppingList[0].id, true);
    setProductPrice(shoppingList[0].id, 2);
    console.assert(shoppingList[0].pricePerUnit === 2, "setProductPrice failed");

    const cost = calculateShoppingCost(new Date().toISOString());
    console.assert(cost.totalCost === 8, "calculateShoppingCost failed");

    bulkModifyProducts([shoppingList[0].id], (product => product.quantity = 10));
    console.assert(shoppingList[0].quantity === 10, "bulkModifyProducts failed");

    console.log("All tests completed.");
}

runTests();
