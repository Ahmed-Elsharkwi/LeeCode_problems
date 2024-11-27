/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let index_1 = s.length - 1;
    let index_2 = t.length - 1;
    let char_1;
    let char_2;

    function helper_fun(string, index) {
        let back_space = 0;

        while (index >= 0) {
            if (back_space == 0 && string[index] != '#') {
                break;
            }
            else if (string[index] == '#') {
                back_space += 1;
            }
            else {
                back_space -= 1;
            }
            index -= 1;
        }
        return index;
    }
    while (true) {
      index_1 = helper_fun(s, index_1);
      index_2 = helper_fun(t, index_2);

      char_1 = index_1 >= 0 ? s[index_1] : '';
      char_2 = index_2 >= 0 ? t[index_2] : '8';
      if (index_1 < 0 && index_2 < 0) {
        break;
      }
      if (char_1 != char_2) {
        return false
      }
      index_1 -= 1
      index_2 -= 1

    }
    return true;
};
