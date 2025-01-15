function dirReduc(arr) {
    // ...
    /**
    1. jika ke UTARA dan index+1 ADALAH SELATAN, maka hapus 2 array tersebut
    2. begitu juga jika BARAT dan index+1 nya adalah TIMUR, maka hapus 2 array tersebut
    3. sebaliknya juga, jika SELATAN ke UTARA atau TIMUR ke BARAT
    
    */

    const directions = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST",
    };

    let result = [];

    for (let i = 0; i < arr.length; i++) {
        const direction = arr[i];
        const opositeDirection = directions[direction];

        if (arr[i + 1] === opositeDirection) {
            arr[i] = null;
            arr[i + 1] = null;
        }
    }

    // return arr.filter(a => a != null);

    return [];
}

console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]));
console.log(["WEST"]);

console.log(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]));
console.log(["NORTH", "WEST", "SOUTH", "EAST"]);

console.log(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"]));
console.log([]);