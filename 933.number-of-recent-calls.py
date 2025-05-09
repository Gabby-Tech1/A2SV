#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.calls = []

        

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.pop(0)
        return len(self.calls)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

