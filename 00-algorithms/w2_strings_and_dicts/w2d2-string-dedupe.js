/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

const str1 = 'abcABC';
const expected1 = 'abcABC';

const str2 = 'helloo';
const expected2 = 'helo';

const str3 = '';
const expected3 = '';

const str4 = 'aa';
const expected4 = 'a';

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
  let output = '';

  for (const char of str) {
    if (!output.includes(char)) {
      output += char;
    }
  }

  return output;
}

console.log(stringDedupe(str1), 'should equal', expected1);
console.log(stringDedupe(str2), 'should equal', expected2);
console.log(stringDedupe(str3), 'should equal', expected3);
console.log(stringDedupe(str4), 'should equal', expected4);
