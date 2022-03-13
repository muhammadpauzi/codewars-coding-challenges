function rot(strng) {
    let result = '';
    for (let i = strng.length - 1; i >= 0; i--) {
        result += strng[i];
    }
    return result;
    // best way
    // return s.split("").reverse().join("");
}

function selfieAndRot(strng) {
    const splitedString = strng.split('\n');
    const repeatedDots = '.'.repeat(splitedString[0].length);
    strng = splitedString.join(repeatedDots + '\n') + repeatedDots;
    return strng + '\n' + rot(strng);
}

function oper(fct, s) {
    return fct(s);
}

// console.log(
//     oper(rot, 'fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL'),
//     'LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif'
// );
// console.log(oper(rot, 'rkKv\ncofM\nzXkh\nflCB'), 'BClf\nhkXz\nMfoc\nvKkr');
console.log(
    oper(selfieAndRot, 'xZBV\njsbS\nJcpN\nfVnP'),
    '\nxZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx'
);
// console.log(
//     oper(selfieAndRot, 'uLcq\nJkuL\nYirX\nnwMB'),
//     'uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu'
// );
