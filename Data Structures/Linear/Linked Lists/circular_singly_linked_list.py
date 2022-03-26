
"""
======================= Circular Singly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Same as Singly Linked List but we have to optmize it to avoid infinite looping.

Node class Variables:
    value: value of current node
    next: whole next Node

Circular Singly Linked List class variables:
    head: the whole node of current singly linked list head

Circular Singly Linked List Methods:

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

    def __init__(self,data = None,next = None) -> None:
        self.value = data
        self.next = next

class CircularSinglyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertAtStart(self, data):

        if self.head is None:
            temp_node = Node(data)
            self.head = temp_node
            self.head.next = self.head
            return

        temp_node = Node(data,self.head)
        

        currentNode = self.head 
        while currentNode.next != self.head:
            currentNode = currentNode.next

        self.head = temp_node
        currentNode.next = self.head

    def insertAtEnd(self,data):

        if self.head is None:
            self.insertAtStart(data)
            return

        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next

        temp_node = Node(data)
        temp_node.next = self.head

        current_node.next = temp_node

    def printAll(self):

        current_node = self.head
        csll_str = ''
        while True:
            if current_node.next != self.head:
                csll_str = csll_str + str(current_node.value) + "======>"
            else:
                csll_str = csll_str + str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

        print(csll_str)

    def getSize(self):

        count = 0
        current_node = self.head

        if current_node is None:
            return 0

        if current_node.next == self.head:
            return 1
        

        while current_node.next != self.head:
            count,current_node = count+1,current_node.next

        return count+1


    def insert(self,index,data):

        if index > self.getSize() or index < 0:
            raise Exception("Invalid Index!")

        if index == 0:
            return self.insertAtStart(data)

        if index == self.getSize():
            return self.insertAtEnd(data)

        current_node = self.head
        i = 0
        while i< index -1:
            current_node = current_node.next
            i = i+1

        temp_node = Node(data,current_node.next)
        current_node.next = temp_node

    def find(self,data):

        index, current_node = 0, self.head
        while index < self.getSize():
            if current_node.value == data:
                return index
            index, current_node = index+1, current_node.next

        return "Not found!"
    
    def insertAfter(self, after_value, data):

        after_value_index = self.find(after_value)
        if after_value == "Not found!":
            raise Exception("Invalid after value")
            
        else:
            self.insert(after_value_index+1, data)


    def insertList(self,data_list):

        for data in data_list:
            self.insertAtEnd(data)

    def removeByValue(self, data):

        current_node = self.head

        if current_node is None:
            raise Exception("Linked List is empty!")

        if current_node.value == data and self.getSize() == 1:
            self.head = None
            return

        if current_node.value == data:
            old = self.head
            self.head = current_node.next

            while current_node.next != old:
                current_node = current_node.next

            current_node.next = self.head

            return

        i = 0
        while i < self.getSize()-1:
            if current_node.next.value == data:
                break
            i, current_node = i+1, current_node.next

        if i!= self.getSize()-2:
            current_node.next = current_node.next.next
        
        else:
            current_node.next = self.head

    def getFirstNode(self):

        return self.head

    def getLastNode(self):

        i = 0
        current_node = self.head
        while i < self.getSize()-1:
            current_node = current_node.next
            i = i+1

        return current_node

    def removeByIndex(self, index):

        if index < 0 or index > self.getSize()-1:
            raise Exception("Invalid Index!")

        if index == 0:
            return self.removeByValue(self.head.value)

        if index == self.getSize()-1 and self.find(self.getLastNode().value) == self.getSize()-1:
            
            return self.removeByValue(self.getLastNode().value)

        i = 0
        current_node = self.head
        while i != index-1:
            current_node,i = current_node.next , i+1
        current_node.next = current_node.next.next



csll = CircularSinglyLinkedList()

print("Size:",csll.getSize())

# csll.insertAtEnd(8)
# csll.printAll()
# print("Size:",csll.getSize())

csll.insertAtStart(16)
csll.printAll()
print("Size:",csll.getSize())

csll.insertAtEnd(4)
csll.printAll()
print("Size:",csll.getSize())

csll.insertAtEnd(2)
csll.printAll()
print("Size:",csll.getSize())

csll.insertAtStart(64)
csll.printAll()
print("Size:",csll.getSize())

csll.insert(4,1)
csll.printAll()
print("Size:",csll.getSize())

csll.insert(0,128)
csll.printAll()
print("Size:",csll.getSize())

csll.insert(2,32)
csll.printAll()
print("Size:",csll.getSize())

print(csll.find(8))
print(csll.find(322))

csll.insertAtStart(512)
csll.printAll()
print("Size:",csll.getSize())

csll.insertAfter(512,256)
csll.printAll()
print("Size:",csll.getSize())

csll.insertList(range(2,11,2))
csll.printAll()
print("Size:",csll.getSize())

csll.removeByValue(10)
csll.printAll()
print("Size:",csll.getSize())

print("First Node Value: ", csll.getFirstNode().value, "Second Node Value: ", csll.getFirstNode().next.value)
print("Last Node Value: ", csll.getLastNode().value, "Circular First Node Value: ", csll.getLastNode().next.value)
csll.printAll()
print("Size:",csll.getSize())

csll.removeByIndex(12)
csll.printAll()
print("Size:",csll.getSize())
print("First Node Value: ", csll.getFirstNode().value, "Second Node Value: ", csll.getFirstNode().next.value)
print("Last Node Value: ", csll.getLastNode().value, "Circular First Node Value: ", csll.getLastNode().next.value)