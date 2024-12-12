/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
  let right = 1;
  let left = 0;
  let max_length = 1

  while(left < s.length && right < s.length) {
    let count = 0;
    for (let idx = left; idx <= right; idx++) {
        if (s[idx] == s[right]) {
            count += 1;
        }
    }
    if (count <= 2) {
        max_length = Math.max(max_length, Math.abs(right - left) + 1);
        right++;
    }
    else {
        left += 1;
        right = left + 1;
    }
  } 
  return max_length; 
};
