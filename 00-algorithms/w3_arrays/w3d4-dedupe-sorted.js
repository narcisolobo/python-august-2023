/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.

  Ok to use a new array

  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
function dedupeSorted(nums) {
  const deduped = [];
  for (const num of nums) {
    if (num !== deduped[deduped.length - 1]) {
      deduped.push(num);
    }
  }
  return deduped;
}

console.log(dedupeSorted(nums1), 'should equal', expected1);
console.log(dedupeSorted(nums2), 'should equal', expected2);
console.log(dedupeSorted(nums3), 'should equal', expected3);
console.log(dedupeSorted(nums4), 'should equal', expected4);

function dedupeSortedInPlace(nums) {
  let placeholder = 0;
  let current = nums[0];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== current) {
      nums[placeholder] = nums[i];
      placeholder++;
      current = nums[i];
    } else {
      temp = nums[i];
      nums[i] = nums[nums.length - 1];
      nums[nums.length - 1] = temp;
      nums.length--;
    }
  }
  return nums;
}

console.log(dedupeSortedInPlace(nums1), 'should equal', expected1);
console.log(dedupeSortedInPlace(nums2), 'should equal', expected2);
console.log(dedupeSortedInPlace(nums3), 'should equal', expected3);
console.log(dedupeSortedInPlace(nums4), 'should equal', expected4);
