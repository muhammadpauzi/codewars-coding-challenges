/**
 * https://www.codewars.com/kata/523f5d21c841566fde000009/train/javascript
 */

export function arrayDiff(a = [], b) {
    return a.filter((a) => !b.includes(a));
}
