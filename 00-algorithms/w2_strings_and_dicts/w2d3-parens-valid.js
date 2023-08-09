/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = 'Y(3(p)p(3)r)s';
const expected1 = true;

const str2 = 'N(0(p)3';
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = 'N(0)t ) 0(k';
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = 'a(b))(c';
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
  const stack = [];

  for (const char of str) {
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}

console.log(parensValid(str1), 'should equal', expected1);
console.log(parensValid(str2), 'should equal', expected2);
console.log(parensValid(str3), 'should equal', expected3);
console.log(parensValid(str4), 'should equal', expected4);
