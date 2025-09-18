class MapSum:

    def __init__(self):
        self.array = {}
        self.end_word = False
        self.value = 0
        

    def insert(self, key: str, val: int) -> None:
        current = self
        for letter in key:
            if letter not in current.array:
                current.array[letter] = MapSum()
            
            current = current.array[letter]
        current.end_word = True
        current.value = val


    def sum(self, prefix: str) -> int:
        def recursion(ptr):
            result = 0
            if len(ptr.array) == 0 and ptr.end_word:
                result += ptr.value
                return result

            for letter in ptr.array:
                result += recursion(ptr.array[letter])

            if ptr.end_word:
                result += ptr.value
            return result

        sumition = 0
        current = self

        for letter in prefix:
            if letter not in current.array:
                return 0
            current = current.array[letter]

        
        
        print(current.array)
        for letter in current.array:
            sumition += recursion(current.array[letter])

        if current.end_word:
                sumition += current.value            
        return sumition


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
