/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = 'object oriented programming';
const expected1 = 'OOP';

// The 4 pillars of OOP
const str2 = 'abstraction polymorphism inheritance encapsulation';
const expected2 = 'APIE';

const str3 = 'software development life cycle';
const expected3 = 'SDLC';

// Bonus: ignore extra spaces
const str4 = '  global   information tracker    ';
const expected4 = 'GIT';

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {String} str A string to be turned into an acronym.
 * @returns {String} The acronym.
 */
function acronymize(str) {
  str = str.trim();
  let acronym = '';

  for (let char = 0; char < str.length; char++) {
    let acronym = '';
    const wordsArr = str.split(' ');

    for (const word of wordsArr) {
      if (word !== '') {
        acronym += word[0].toUpperCase();
      }
    }
    return acronym;
  }
  return acronym;
}

const result1 = acronymize(str1);
console.log(result1);

const result2 = acronymize(str2);
console.log(result2);

const result3 = acronymize(str3);
console.log(result3);

const result4 = acronymize(str4);
console.log(result4);
