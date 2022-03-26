
"""
======================= Circular Doubly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Same as Doubly Linked List but we have to optmize it to avoid infinite looping.

Node class Variables:
    value: value of current node
    next: whole next Node
    prev: whole previous node

Circular Doubly Linked List class variables:
    head: the whole node of current singly linked list head

Circular Doubly Linked List Methods:

insertAtStart(data) # insert Node at start

printAll() # print every element of current linked list

getSize() # return length of current Linked List

insertAtEnd(data) # insert Node at end

insert(index, data) # insert Node at the given index

insertAfter(after_value, data) # insert Node after given after_value

insertList(list) # insert bulk data of list

removeByValue(data) # remove first occurence of given value

removeByIndex(index) #remove Node by Index

find(data) #return index of first occurence of given value

getFirstNode() # return whole first node

getLastNode() # return whole last node (the last node pointers to self.head (first node))

"""

class Node:

    def __init__(self, data = None, next = None, prev = None) -> None:
        self.value = data
        self.next = next
        self.prev = prev


class CircularDoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertAtStart(self, data):

        if self.head is None:
            temp_node = Node(data)
            self.head = temp_node
            self.head.prev = self.head
            self.head.next = self.head
            
            return


        last_node = self.head
        
        while last_node.next != self.head:
            last_node = last_node.next

        first_node = self.head

        temp_node = Node(data, first_node, last_node)

        last_node.next = temp_node

        first_node.prev = temp_node

        self.head = temp_node
        



    def printAll(self):
        
        current_node = self.head
        cdll = ''
        while True:
            print("Previous Node:",current_node.prev.value,"Current Node:",current_node.value,"Next Node:",current_node.next.value)
            if current_node.next == self.head:
                cdll = cdll + str(current_node.value)
            else:
                cdll = cdll + str(current_node.value) + "=======>"

            current_node = current_node.next
            if current_node == self.head:
                break

        print(cdll)

    def insertAtEnd(self,data):

        if self.head is None:
            return self.insertAtStart(data)

        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next

        temp_node = Node(data,self.head,current_node)

        current_node.next = temp_node
        self.head.prev = temp_node

    def getSize(self):

        if self.head is None:
            return 0

        currentNode = self.head.prev
        count = 1
        while currentNode.prev != self.head:
            count = count+1
            currentNode = currentNode.prev

        return count+1

    def insert(self, index, data):

        if index < 0 or index > self.getSize():

            raise Exception("Invalid Index!")

        if index == 0:
            return self.insertAtStart(data)

        if index == self.getSize():
            return self.insertAtEnd(data)

        count = 0
        current_node = self.head

        while count != index-1:
            current_node = current_node.next
            count = count +1

        temp_node = Node(data,current_node.next, current_node)
        current_node.next.prev = temp_node
        current_node.next = temp_node

    def find(self, data):

        count = 0
        current_node = self.head
        while count < self.getSize():
            if current_node.value == data:
                return count
            current_node = current_node.next
            count = count+1

        return "Not found!"

    def getFirstNode(self):
        if self.head is None:
            return "Linked List is empty!"
        return self.head

    def getLastNode(self):
        if self.head is None:
            return "Linked List is empty!"
        return self.head.prev

    def insertList(self,data_list):

        for data in data_list:
            self.insertAtStart(data)

    def insertAfter(self,after_value, data):

        after_value_index = self.find(after_value)
        try:
            self.insert(after_value_index+1, data)
        except TypeError:
            raise Exception("Invalid after value")


    def removeByIndex(self, index):

        if index == 0:

            old_head = self.head
            self.head = self.head.next
            self.head.prev = old_head.prev
            self.head.prev.next = self.head
            return

        if index == self.getSize()-1:

            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
            return

        i = 0
        current_node = self.head
        while i<index -1:
            i = i+1
            current_node = current_node.next

        current_node.next = current_node.next.next
        current_node.next.prev = current_node

    def removeByValue(self, data):


        if self.head.value == data:
            
            return self.removeByIndex(0)

        find_index = self.find(data)

        if find_index == "Not found!":
            raise Exception("Value does not exist!")

        if find_index == self.getSize()-1:
            return self.removeByIndex(find_index)

        current_node = self.head
        index = 0
        while True:
            if current_node.value == data:
                break
            current_node = current_node.next
            index = index +1

        return self.removeByIndex(index)

cdll = CircularDoublyLinkedList()

print("Size:", cdll.getSize())

cdll.insertAtStart(20)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insertAtStart(10)
cdll.printAll()
print("Size:", cdll.getSize())


cdll.insertAtStart(5)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insertAtEnd(50)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insertAtEnd(100)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insert(4,80)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insertAtStart(2)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insert(0,1)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.removeByValue(80)
cdll.printAll()
print("aaaaaSize:", cdll.getSize())

cdll.insertAtEnd(200)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insert(8,250)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insert(7,150)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.insertAtEnd(500)
cdll.printAll()
print("Size:", cdll.getSize())

print("Index: ", cdll.find(500))

cdll.insertAfter(250,400)
cdll.printAll()
print("Size:", cdll.getSize())

cdll.removeByIndex(5)
cdll.printAll()
print("Size:", cdll.getSize())

