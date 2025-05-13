#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)

        return len(stack)
        
# @lc code=end

