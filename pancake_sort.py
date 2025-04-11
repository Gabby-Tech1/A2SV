class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flips = []
        n = len(arr)

        for i in range(n, 1, -1):
            max_index = arr.index(max(arr[:i]))
            
            if max_index != i - 1: 
                if max_index != 0:
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                    flips.append(max_index + 1)

                arr[:i] = arr[:i][::-1]
                flips.append(i)
            
        return flips
