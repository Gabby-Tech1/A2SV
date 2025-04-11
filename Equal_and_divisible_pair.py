class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0  # Initialize counter for valid pairs
        
        # Use a nested loop to check all possible pairs (i, j) where i < j
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the values are equal AND (i * j) is divisible by k
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count

