// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper2(collection, itemsPerPage) {
    let tempCollection = [];
    this.collection = [];
    this.itemsPerPage = itemsPerPage;

    for (let i = 0; i < collection.length; i++) {
        tempCollection.push(collection[i]);
        if (
            tempCollection.length === itemsPerPage ||
            collection[i + 1] === undefined
        ) {
            this.collection.push(tempCollection);
            tempCollection = [];
        }
    }
}

// returns the number of items within the entire collection
PaginationHelper2.prototype.itemCount = function () {
    return this.collection
        .map((col) => col.length)
        .reduce((prev, cur) => prev + cur);
};

// returns the number of pages
PaginationHelper2.prototype.pageCount = function () {
    return this.collection.length;
};

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper2.prototype.pageItemCount = function (pageIndex) {
    const pageOfCollection = this.collection[pageIndex];
    return pageOfCollection ? pageOfCollection.length : -1;
};

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper2.prototype.pageIndex = function (itemIndex) {
    let total = 0;
    for (let i = 0; i < this.collection.length; i++) {
        for (let j = 0; j < this.collection[i].length; j++) {
            if (total === itemIndex) return i;
            total++;
        }
    }
    return -1;
};

export default PaginationHelper2;

// Best Way
function PaginationHelper2(collection, itemsPerPage) {
    (this.collection = collection), (this.itemsPerPage = itemsPerPage);
}

PaginationHelper2.prototype.itemCount = function () {
    return this.collection.length;
};

PaginationHelper2.prototype.pageCount = function () {
    return Math.ceil(this.collection.length / this.itemsPerPage);
};

PaginationHelper2.prototype.pageItemCount = function (pageIndex) {
    return pageIndex < this.pageCount()
        ? Math.min(
              this.itemsPerPage,
              this.collection.length - pageIndex * this.itemsPerPage
          )
        : -1;
};

PaginationHelper2.prototype.pageIndex = function (itemIndex) {
    return itemIndex < this.collection.length && itemIndex >= 0
        ? Math.floor(itemIndex / this.itemsPerPage)
        : -1;
};
