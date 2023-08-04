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
  // your pseudo code
  // your awesome code
}

/* 
  Longest Palindromic Substring

  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 

  Strings longer or shorter than complete words are OK.

  All the substrings of "abc" are:
  a, ab, abc, b, bc, c

  If there is more than one palindromic substring of the same longest length,
  return the first palindromic substring.
*/

const str5 = 'what up, daddy-o?';
const expected5 = 'dad';

const str6 = 'uh, not much';
const expected6 = 'u';

const str7 = 'Yikes! my favorite racecar erupted!';
const expected7 = 'e racecar e';

const str8 = 'a1001x20002y5677765z';
const expected8 = '5677765';

const str9 = 'a1001x20002y567765z';
const expected9 = '567765';

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
  // your pseudo code
  // your awesome code
}
