const toWeirdCase = (string) => string.split(' ')
    .map((word, i) => word
        .split('')
        .map((char, j) => j % 2 === 0 ? char.toUpperCase() : char.toLowerCase()).join('')
    ).join(' ');

// let results = '';

// for (let i = 0; i < string.length; i++) {
//     const char = string[i];
//     results += i % 2 === 0 ? char.toUpperCase() : char.toLowerCase();
// }

// return results;

console.log(toWeirdCase('This'), 'ThIs');
console.log(toWeirdCase('is'), 'Is');
console.log(toWeirdCase('This is a test'), 'ThIs Is A TeSt');