#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next
        # The next node is now deleted, as it is no longer referenced
        # and will be garbage collected when it goes out of scope.
        # This is a common technique to delete a node in a singly linked list
        # when you are given a reference to that node.
        # Note: This method only works if the node to be deleted is not the last node.
        # If the node to be deleted is the last node, we cannot delete it in this way.
        # In that case, we would need to traverse the list to find the previous node
        
# @lc code=end

