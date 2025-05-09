#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)

        return score
        
# @lc code=end

