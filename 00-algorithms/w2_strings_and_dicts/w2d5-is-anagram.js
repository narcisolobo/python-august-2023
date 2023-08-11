/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Is there a quick way to determine if they aren't an anagram before spending more time?

  Given two strings
  return whether or not they are anagrams
*/

const strA1 = 'yes';
const strB1 = 'eys';
const expected1 = true;

const strA2 = 'yes';
const strB2 = 'eYs';
const expected2 = true;

const strA3 = 'no';
const strB3 = 'noo';
const expected3 = false;

const strA4 = 'silent';
const strB4 = 'listen';
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
  if (s1.length !== s2.length) {
    return false;
  }

  const freq1 = {};
  const freq2 = {};

  for (const char of s1) {
    if (!freq1.hasOwnProperty(char)) {
      freq1[char] = 1;
    } else {
      freq1[char]++;
    }
  }

  for (let char of s2) {
    char = char.toLowerCase();
    if (!freq2.hasOwnProperty(char)) {
      freq2[char] = 1;
    } else {
      freq2[char]++;
    }
  }

  for (let char in freq1) {
    char = char.toLowerCase();
    if (freq1[char] !== freq2[char]) {
      return false;
    }
  }

  return true;
}

console.log(isAnagram(strA1, strB1), 'should equal', expected1);
console.log(isAnagram(strA2, strB2), 'should equal', expected2);
console.log(isAnagram(strA3, strB3), 'should equal', expected3);
console.log(isAnagram(strA4, strB4), 'should equal', expected4);
