/* 
  String: Reverse

  Given a string, return a new string that is
  the given string reversed
*/

const str1 = 'creature';
const expected1 = 'erutaerc';

const str2 = 'dog';
const expected2 = 'god';

const str3 = 'hello';
const expected3 = 'olleh';

const str4 = '';
const expected4 = '';

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
  let reversed = '';

  for (let char = str.length - 1; char >= 0; char--) {
    reversed += str[char];
  }
  return reversed;
}

const result1 = reverseString(str1);
console.log(result1);

const result2 = reverseString(str2);
console.log(result2);

const result3 = reverseString(str3);
console.log(result3);

const result4 = reverseString(str4);
console.log(result4);
