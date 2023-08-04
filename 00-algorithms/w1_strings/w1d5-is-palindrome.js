/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is the same forwards and backwards
  
  Do not ignore spaces, punctuation or capitalization
 */

const str1 = 'a x a';
const expected1 = true;

const str2 = 'racecar';
const expected2 = true;

const str3 = 'Dud';
const expected3 = false;

const str4 = 'oho!';
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
  for (var left = 0; left < str.length / 2; left++) {
    var right = str.length - 1 - left;
    if (str[left] != str[right]) {
      return false;
    }
  }
  return true;
}

const result1 = isPalindrome(str1);
console.log(result1);

const result2 = isPalindrome(str2);
console.log(result2);

const result3 = isPalindrome(str3);
console.log(result3);

const result4 = isPalindrome(str4);
console.log(result4);

module.exports = { isPalindrome };
