const {
    addProduct,
    removeProduct,
    editProductName,
    editProductQuantity,
    editProductDueDate,
    editProductStatus,
    setProductPrice,
    calculateShoppingCost,
    shoppingList
  } = require("./shoppingList");
  
  function runTests() {
    console.log("Running tests...");
  

    addProduct("Milk", 2, "2025-04-05");
    console.assert(shoppingList.length === 1, "addProduct failed");
    console.assert(shoppingList[0].name === "Milk", "addProduct name failed");
  
    const id = shoppingList[0].id;
    removeProduct(id);
    console.assert(shoppingList.length === 0, "removeProduct failed");
  
    addProduct("Butter", 1, "2025-04-05");
    const butterId = shoppingList[0].id;
    editProductName(butterId, "Margarine");
    console.assert(shoppingList[0].name === "Margarine", "editProductName failed");
  
    editProductQuantity(butterId, 3);
    console.assert(shoppingList[0].quantity === 3, "editProductQuantity failed");
  
    editProductDueDate(butterId, "2025-04-10");
    console.assert(
      shoppingList[0].dueDate.toDateString() === new Date("2025-04-10").toDateString(),
      "editProductDueDate failed"
    );
  
    editProductStatus(butterId, true);
    console.assert(shoppingList[0].purchased === true, "editProductStatus failed");
  
    setProductPrice(butterId, 5);
    console.assert(shoppingList[0].pricePerUnit === 5, "setProductPrice failed");
  
    const cost = calculateShoppingCost("2025-04-10");
    console.assert(cost.totalCost === 15, "calculateShoppingCost failed");
  
    console.log("All tests completed!");
  }
  
  runTests();
  