import PaginationHelper from './paginationHelper.js';
import { describe, it } from 'mocha';
import { assert } from 'chai';

// const helper = new PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4);
// const helper = new PaginationHelper([], 4);
const helper = new PaginationHelper(
    [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24,
    ],
    10
);
console.log(helper.itemCount());
// console.log(helper.pageCount());
// console.log(helper.pageItemCount(1));
// console.log(helper.pageItemCount(0));
// console.log(helper.pageItemCount(3));
// console.log(helper.pageIndex(0));
// console.log(helper.pageIndex(2));
// console.log(helper.pageIndex(5));
// console.log(helper.pageIndex(6));
// console.log(helper.pageIndex(7));

// describe('Solution', function () {
//     it('test create new object of Pagination Helper', function () {
//         assert.deepEqual(
//             new PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4).collection,
//             [
//                 ['a', 'b', 'c', 'd'],
//                 ['e', 'f'],
//             ]
//         );
//         assert.deepEqual(
//             new PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 1).collection,
//             [['a'], ['b'], ['c'], ['d'], ['e'], ['f']]
//         );
//         assert.deepEqual(new PaginationHelper(['a', 'b'], 2).collection, [
//             ['a', 'b'],
//         ]);
//         assert.deepEqual(new PaginationHelper(['a'], 2).collection, [['a']]);
//     });
// });
