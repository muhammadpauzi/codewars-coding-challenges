function repeater(string, n) {
    // let str = '';
    // for (let i = 0; i < n; i++) {
    //     str += string;
    // }

    // return str

    // Top best solution
    string.repeat(n)
}

print(repeater('a', 5), 'aaaaa')
print(repeater('Na', 16), 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa')
print(repeater('Wub ', 6), 'Wub Wub Wub Wub Wub Wub ')