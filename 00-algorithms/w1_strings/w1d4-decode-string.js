/* 
  String Decode  
*/

const str1 = 'a3b2c1d3';
const expected1 = 'aaabbcddd';

const str2 = 'a3b2c12d10';
const expected2 = 'aaabbccccccccccccdddddddddd';

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
  let decoded = '';
  let currentChar = '';

  for (let char = 0; char < str.length; char++) {
    let digits = '';

    if (isNaN(str[char])) {
      currentChar = str[char];
      char++;

      while (!isNaN(str[char])) {
        digits += str[char];
        char++;
      }
    }
    for (let i = 1; i <= parseInt(digits); i++) {
      decoded += currentChar;
    }

    char--;
  }
  return decoded;
}

result1 = decodeStr(str2);
console.log(result1);
