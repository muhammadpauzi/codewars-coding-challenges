// https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa

function isMerge(s, part1, part2) {

    if (s.length > (part1.length + part2.length)) return false;

    let result = true;
    const sChars = s.split('');

    const lengthPerChar = new Map();
    sChars.map(char => {
        if (!lengthPerChar.has(char)) { // only first
            lengthPerChar.set(char, sChars.filter(schar => schar == char).length);
        }
    });

    const twoPartsChars = (part1 + part2).split('');

    twoPartsChars.map(char => {
        const count = twoPartsChars.filter(schar => schar == char).length;
        if (count != lengthPerChar.get(char)) return result = false;
    });

    return result;
}

console.log(true, isMerge('xcyc', 'xc', 'yc'));
console.log(true, isMerge('xcyc', 'yc', 'xc'));
console.log(true, isMerge('xcyc', 'xc', 'cy'));
console.log(true, isMerge('xcyc', 'cy', 'xc'));

console.log(true, isMerge('codewars', 'code', 'wars'));
console.log(true, isMerge('codewars', 'code', 'wasr'));
console.log(true, isMerge('codewars', 'cdwr', 'oeas'));
console.log(true, isMerge('Making progress', 'Mak pross', 'inggre'));
console.log(false, isMerge('codewars', 'code', 'code'));
console.log(false, isMerge('More progress', 'More ess', 'pro'));