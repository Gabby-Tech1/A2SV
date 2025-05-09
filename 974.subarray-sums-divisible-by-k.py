#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_sum = 0
        mod_count = {0: 1}
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:
                mod += k
            if mod in mod_count:
                count += mod_count[mod]
                mod_count[mod] += 1
            else:
                mod_count[mod] = 1
        return count
        
# @lc code=end

