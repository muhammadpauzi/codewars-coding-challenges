function oneDown(str) {
    if (typeof str !== "string") return "Input is not a string";

    let results = "";

    for (let i = 0; i < str.split("").length; i++) {
        let code = str.charCodeAt(i);

        if (code == 32) {
            results += " ";
            continue;
        }

        if (code == 97) {
            results += "Z";
            continue;
        }

        if (code == 65) {
            results += "z";
            continue;
        }

        if (code >= 65 && code <= 90) {
            code -= 1;
        }

        if (code >= 97 && code <= 122) {
            code -= 1;
        }

        results += String.fromCharCode(code);
    }

    return results;
}

// best solution
// function oneDown2(str) {
//     var alph = "zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

//     return typeof str === "string" ? str.replace(/\w/g, v => alph.charAt(alph.lastIndexOf(v) - 1)) : "Input is not a string";
// }


// console.log(oneDown2("Ifmmp"), "Hello");

console.log(oneDown("Ifmmp"), "Hello");
console.log(oneDown("Uif usjdl up uijt lbub jt tjnqmf"), "The trick to this kata is simple");
console.log(oneDown(45), "Input is not a string");


