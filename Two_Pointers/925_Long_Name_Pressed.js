/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    let length_name = name.length;
    let typed_length = typed.length;
    let name_ptr = 0;
    let typed_ptr = 0;

    while ((name_ptr != length_name) && (typed_ptr != typed_length)){
        
        if (name[name_ptr] == typed[typed_ptr]){
            name_ptr += 1;
        }
        else{
            if (typed_ptr != 0){
                if ((typed[typed_ptr - 1] != typed[typed_ptr]) && (typed[typed_ptr + 1] != typed[typed_ptr])){
                    console.log(typed[typed_ptr]);
                    return false
                }
            }
        }
        if (name_ptr == 0){
            return false
        }
        typed_ptr += 1;
    }
    if (name_ptr != length_name){
        return false
    }
    typed
    while (typed_ptr != typed_length){
        if (typed[typed_ptr] != typed[typed_ptr - 1]){
            return false
        }
        typed_ptr += 1
    }
    return true
    
};
