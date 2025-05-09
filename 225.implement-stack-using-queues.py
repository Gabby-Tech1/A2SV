#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)    
        

    def pop(self) -> int:
        pass
        

    def top(self) -> int:
        pass
        

    def empty(self) -> bool:
        pass


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

