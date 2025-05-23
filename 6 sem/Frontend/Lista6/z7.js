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

const addBooksToLibrary = (books) => {
    books.forEach(book => {
        addBookToLibrary(...book);
    });
};

const books = [
    ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
    ["1984", "George Orwell", 300, true, [4, 5]],
    ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
    ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
    ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
    ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
    ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
    ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
    ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
    ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
];

addBooksToLibrary(books);
console.log(library);
  