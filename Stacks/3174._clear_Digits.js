/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    let new_str = [];
    let new_s = ""
    let index = -1;

    for (let idx = 0; idx < s.length; idx++) {
        if ((s[idx] >= 0 && s[idx] <= 9) && (index != -1)) {
            new_str.pop();
        }
        else {
            new_str.push(s[idx]);
            index++;
        }
    }
    for (let index = 0; index < new_str.length; index++) {
        new_s += new_str[index];
    }
    return new_s;
};
