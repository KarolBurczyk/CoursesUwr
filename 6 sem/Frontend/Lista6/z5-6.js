let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
    if (typeof title !== "string" || title.trim() === "") {
        throw new Error("Title must be a non-empty string");
    }
    if (typeof author !== "string" || author.trim() === "") {
        throw new Error("Author must be a non-empty string");
    }
    if (typeof pages !== "number" || pages <= 0) {
        throw new Error("Pages must be a positive number");
    }
    if (typeof isAvailable !== "boolean") {
        throw new Error("isAvailable must be a boolean");
    }
    if (!Array.isArray(ratings)) {
        throw new Error("Ratings must be an array");
    }
    if (ratings.some(rating => typeof rating !== "number" || rating < 0 || rating > 5)) {
        throw new Error("Ratings must be an array of numbers between 0 and 5");
    }
  
    library.push({
        title,
        author,
        pages,
        available: isAvailable,
        ratings,
    });
};

const testAddingBooks = (testCases) => {
    testCases.forEach(({ testCase, shouldFail }) => {
        try {
            addBookToLibrary(...testCase);
            if (shouldFail) {
                console.log(`Test failed: ${JSON.stringify(testCase)}`);
            } else {
                console.log(`Test passed: ${JSON.stringify(testCase)}`);
            }
        } catch (error) {
            if (shouldFail) {
                console.log(`Test passed: ${JSON.stringify(testCase)}, Error: ${error.message}`);
            } else {
                console.log(`Test failed: ${JSON.stringify(testCase)}, Error: ${error.message}`);
            }
        }
    });
};
  

const testCases = [
    { testCase: ["", "Author", 200, true, []], shouldFail: true },
    { testCase: ["Title", "", 200, true, []], shouldFail: true },
    { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
    { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]], shouldFail: true, },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]], shouldFail: false, },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]], shouldFail: false, },
];
  
testAddingBooks(testCases);