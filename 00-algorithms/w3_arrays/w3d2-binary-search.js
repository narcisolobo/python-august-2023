/* 
  Array: Binary Search (non recursive)

  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .

  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete

    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

function randomNumber(min = 0, max = 20) {
  return Math.floor(Math.random() * max) + min;
}

function randomSortedArray(length = 10, min = 0, max = 20) {
  const arr = [];
  for (let i = 0; i < length; i++) {
    arr.push(randomNumber(min, max));
  }
  return arr.sort((a, b) => a - b);
}

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
  let low = 0;
  let high = sortedNums.length - 1;

  while (low <= high) {
    let mid = low + Math.floor((high - low) / 2);
    console.log('Mid:', mid, 'Mid:', mid, 'Mid:', mid);

    if (searchNum === sortedNums[mid]) {
      return true;
    } else if (searchNum < sortedNums[mid]) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return false;
}

console.log(binarySearch(nums1, searchNum1), 'should equal', expected1);
console.log(binarySearch(nums2, searchNum2), 'should equal', expected2);
console.log(binarySearch(nums3, searchNum3), 'should equal', expected3);

const randArr = randomSortedArray();
console.log(randArr);
console.log(binarySearch(randArr, 12));
