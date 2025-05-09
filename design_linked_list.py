class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        if index < 0 or self.head == None:
            return -1
            
        curr = self.head
        for i in range(index):
            if curr.next == None:
                return -1
            curr = curr.next
        
        return curr.val

        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        if self.head == None:
            self.head = new_node
            return
            
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
            
        if index == 0:
            self.addAtHead(val)
            return
            
        curr = self.head
        for i in range(index - 1):
            if curr == None:
                return
            curr = curr.next
            
        if curr == None:
            return
            
        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head == None:
            return
            
        if index == 0:
            self.head = self.head.next
            return
            
        curr = self.head
        for i in range(index - 1):
            if curr.next == None:
                return
            curr = curr.next
            
        if curr.next == None:
            return
            
        curr.next = curr.next.next

    def display(self) -> None:
        array = []
        curr = self.head
        while curr != None:
            array.append(curr.val)
            curr = curr.next
        print(array)

my_list = MyLinkedList()       
my_list.display()
my_list.addAtHead(2)
my_list.addAtHead(4)
my_list.addAtHead(5)
my_list.display()
my_list.addAtTail(6)
my_list.addAtTail(7)
my_list.addAtTail(8)
my_list.display()
my_list.addAtIndex(2, 9)
my_list.display()
my_list.addAtIndex(0, 10)
my_list.display()
my_list.addAtIndex(10, 11)
my_list.display()
my_list.deleteAtIndex(0)
my_list.display()
my_list.deleteAtIndex(2)
my_list.display()