function proofread(str) {
    let strs = str.toLowerCase().split(". ");

    strs = strs.map(str => {
        str = str.trim();

        if (!str) return false;

        str = str.replaceAll("ie", "ei");
        str = str[0].toUpperCase() + str.substring(1, str.length);

        return str;
    }).filter(Boolean);

    return strs.join(". ");
}

// best solution
// function proofread(str) { 
//     return str.toLowerCase()
//       .replace(/ie/g, "ei")
//       .replace(/(^|\. )(.)/g, (_, a, b) => a + b.toUpperCase())
//   }

console.log(proofread("ThiEr DEcIEt wAs INconcIEVablE. sHe SIeZeD thE moMENT."), "Their deceit was inconceivable. She seized the moment.");
console.log(proofread("HIs nieghBOur wAs oVerwieGht."), "His neighbour was overweight.");
console.log(proofread("SHe rEcieveD a pIegNor."), "She received a peignor.");
console.log(proofread("He had eight shots of caffeine"), "He had eight shots of caffeine");
