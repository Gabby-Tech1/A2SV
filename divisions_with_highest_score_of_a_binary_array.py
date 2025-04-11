def maxScoreIndices(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        total_ones = sum(nums)
        
        max_score = 0
        result = []
        
        left_zeros = 0
        right_ones = total_ones
        
        for i in range(n + 1):
            current_score = left_zeros + right_ones
            
            if current_score > max_score:
                max_score = current_score
                result = [i]
            elif current_score == max_score:
                result.append(i)

            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1
        
        return result
