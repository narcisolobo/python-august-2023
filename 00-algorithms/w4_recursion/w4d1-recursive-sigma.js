/* 
  Write a recursive function that, given a number,
  returns the sum of integers from one up to that
  number.
  
  For example,
  rSigma(5) = 1 + 2 + 3 + 4 + 5 = 15;
  rSigma(2.5) = 1 + 2 = 3;
  rSigma(-1) = 0.
*/

/* 
Requirements for Recursion
1. Base Case (exit clause - stops the loop)
2. Progression towards base case
3. Call function inside itself
*/

function sigma(num) {
  if (num <= 0) {
    return 0;
  }

  num = Math.floor(num);
  let sum = 0;

  for (let i = 1; i <= num; i++) {
    sum += i;
  }

  return sum;
}

/**
 *
 * @param {number} num
 * @returns {number}
 */
function rSigma(num) {
  if (num < 1) {
    return num;
  }

  num = Math.floor(num);

  return rSigma(num - 1) + num;
}

console.log(sigma(5));
console.log(rSigma(5));
