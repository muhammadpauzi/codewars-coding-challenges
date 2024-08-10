class Vector {

    component = [];

    constructor(component) {
        this.component = component;
    }

    add(vector) {
        if (vector.component.length !== this.component.length) throw new Error("The length should be same.");
        return new Vector(vector.component.map((value, i) => this.component[i] + value));
    }

    subtract(vector) {
        if (vector.component.length !== this.component.length) throw new Error("The length should be same.");
        return new Vector(vector.component.map((value, i) => this.component[i] - value));
    }

    dot(vector) {
        if (vector.component.length !== this.component.length) throw new Error("The length should be same.");
        return vector.component.map((value, i) => this.component[i] * value).reduce((a, b) => a + b);
    }

    norm() {
        return Math.sqrt(this.component.map(value => value * value).reduce((a, b) => a + b, 0));
    }

    equals(vector) {
        if (vector.component.length !== this.component.length) return false;
        return vector.component.every((value, i) => this.component[i] === value);
    }

    toString() {
        return `(${this.component.toString()})`;
    }
}

const a = new Vector([1, 2]);
const b = new Vector([3, 4]);
const c = new Vector([3, 4, 5]);
const d = new Vector([1, 2]);
var e = new Vector([1, 2, 3]);

console.log(a.add(b), new Vector([4, 6]));
console.log(a.subtract(b), new Vector([4, 6]));
console.log(a.dot(b), new Vector([4, 6]));
console.log(e.norm());
console.log(a.equals(b), new Vector([4, 6]));
console.log(a.equals(d), new Vector([4, 6]));
console.log(a.toString());
console.log(a.add(c), "SHOULD BE ERROR");