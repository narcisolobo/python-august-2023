/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ['a', 'a', 'a'];
const expected1 = {
  a: 3,
};

const arr2 = ['a', 'b', 'a', 'c', 'B', 'c', 'c', 'd'];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {
  const freqTable = {};

  for (const elem of arr) {
    if (!freqTable.hasOwnProperty(elem)) {
      freqTable[elem] = 1;
    } else {
      freqTable[elem] += 1;
    }
  }
  return freqTable;
}

/* const result1 = makeFrequencyTable(arr1);
console.log(result1);

const result2 = makeFrequencyTable(arr2);
console.log(result2);

const result3 = makeFrequencyTable(arr3);
console.log(result3); */

module.exports = makeFrequencyTable;
