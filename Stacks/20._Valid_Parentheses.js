/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let CharactersArray = [];
    let index = -1;

    if (s.length <= 1){
        return false
    }

    for (let i = 0; i < s.length; i++) {
        if ((CharactersArray[index] == '(' && s[i] == ')') 
           || (CharactersArray[index] == '{' && s[i] == '}') 
           || (CharactersArray[index] == '[' && s[i] == ']')) {
            CharactersArray.pop();
            index -= 1;
        }
        else {
            CharactersArray.push(s[i]);
            index += 1;
        }
    }
    if (CharactersArray.length == 0){
        return true;
    }
    return false;
};
