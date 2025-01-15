function stockList(books = [], categories = []) {
    if (!books || books.length === 0 || !categories || categories.length === 0) return "";

    let results = [];

    for (let i = 0; i < categories.length; i++) {
        const category = categories[i];
        let quantity = 0;

        for (let j = 0; j < books.length; j++) {
            const book = books[j];

            if (book.charAt(0) === category) {
                quantity += Number(book.split(" ")[1])
            }
        }

        results.push(`(${category} : ${quantity})`)
    }

    return results.join(" - ");
}


function doTest(books, categories, expected) {
    const message = `books = ${JSON.stringify(books)}\ncategories = ${JSON.stringify(categories)}\n`;
    const actual = stockList(books, categories);
    console.log(actual);
    console.log(expected);
}

doTest(
    ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],
    ["A", "B", "C", "D"],
    "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
);
doTest(
    ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
    ["A", "B"],
    "(A : 200) - (B : 1140)"
);