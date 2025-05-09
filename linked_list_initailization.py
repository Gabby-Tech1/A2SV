# Initializing and accessing a node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# # class myLinkedList:
# arr = [2, 3, 5, 6]
# head = Node(arr[2])
# # print(head.value)
# # print(head.next)


# Converting array to linked list
arr = [2, 3, 5, 6]
head = Node(arr[0])
curr = head

# for i in range(1, len(arr)):
#     curr.next = Node(arr[i])
#     curr = curr.next


# traversing the linked list
# curr = head
# arr = []
# while curr != None:
#     print(curr.value)
#     curr = curr.next

# length of the linked list
