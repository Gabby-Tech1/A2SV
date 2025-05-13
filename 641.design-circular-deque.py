#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]
    
    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.rear]
    
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
    

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

