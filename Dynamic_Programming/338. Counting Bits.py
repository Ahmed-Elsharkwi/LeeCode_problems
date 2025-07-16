class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        array = [0, 1]

        if n == 0:
            return [n]
        if n == 1:
            return array
        
        
        for i in range(2, n + 1):
            if i % 2 != 0:
                array.append(1)
            else:
                array.append(0)
            array[i] += array[int(i / 2)]
        return array            

