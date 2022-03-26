

"""
======================= Doubly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Node class Variables:
    value: value of current node
    next: whole next node
    prev: whole previous node


Doubly Linked List class variables:
    head: the whole node of current doubly linked list head


Doubly Linked List Methods:

insertAtStart(data) # insert Node at start

printAll() # print every element of current linked list

printBackward() #print doubly linked list in reverse order

getSize() # return length of current Linked List

insertAtEnd(data) # insert Node at end

insert(index, data) # insert Node at the given index

insertAfter(after_value, data) # insert Node after given after_value

insertList(list) # insert bulk data of list

removeByValue(data) # remove first occurence of given value

removeByIndex(index) #remove Node by Index

find(data) #return index of first occurence of given value

"""


class Node:

    def __init__(self,value = None, next = None, prev = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertAtStart(self,data):

        temp_node = Node(data,self.head)
        if self.head is not None:
            self.head.prev = temp_node
        self.head = temp_node
        

    def printAll(self):

        currentNode = self.head
        dll_str = ''
        while currentNode != None:
            if currentNode.next == None:
                dll_str = dll_str+ str(currentNode.value)
            else:
                dll_str = dll_str+ str(currentNode.value) + "====>"

            currentNode = currentNode.next

        print(dll_str)

    def getSize(self):

        currentNode = self.head
        count = 0

        while currentNode != None:
            count +=1
            currentNode = currentNode.next

        return count

    def insertAtEnd(self,data):

        currentNode = self.head

        while currentNode.next != None:
            currentNode = currentNode.next

        currentNode.next = Node(data,None, currentNode)
        

    def printBackward(self):

        currentNode = self.head

        while currentNode.next !=None:
            
            currentNode = currentNode.next
            

        dll_str_backward = ''

        while currentNode != None:
            
            if currentNode.prev is not None:
                dll_str_backward = dll_str_backward + str(currentNode.value) + "====>"
            else:
                dll_str_backward = dll_str_backward + str(currentNode.value) 

            currentNode = currentNode.prev

        print(dll_str_backward)

    def insert(self,index,data):

        if index < 0 or index > self.getSize():
            raise Exception("Invalid Index")

        if index  == 0:
            self.insertAtStart(data)
            return 

        i = 0
        currentNode = self.head
        while i != index-1:
            currentNode = currentNode.next
            i = i+1

        temp_node = Node(data,currentNode.next,currentNode)
        currentNode.next  = temp_node
        if currentNode.next.next is not None:
            currentNode.next.next.prev = temp_node

        
    def find(self,data):

        currentNode = self.head
        i = 0
        while i< self.getSize():
            if currentNode.value == data:
                return i 
            currentNode = currentNode.next
            i = i+1

        return "Not found!"

    def insertAfter(self,after_value,data):

        after_value_index = self.find(after_value)
        if after_value_index == "Not found!":
            raise Exception("Given After Item does not exist!")
            
        self.insert(after_value_index+1,data)
        
    def insertList(self,list_data):
        
        for data in list_data:
            self.insertAtEnd(data)

    def removeByValue(self,data):

        if self.head.value == data:
            self.head = self.head.next
            self.head.prev = None
            return

        currentNode = self.head

        while currentNode:

            if currentNode.value == data:
                break
            currentNode = currentNode.next

        if currentNode.next:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            return

        currentNode.prev.next = None

    def removeByIndex(self,index):

        if index < 0 or index > self.getSize()-1:
            raise Exception("Invalid Index!")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        i = 0 
        currentNode = self.head
        while i != index:
            currentNode = currentNode.next
            i = i+1

        if currentNode.next != None:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            return

        currentNode.prev.next = None


dll = DoublyLinkedList()

dll.insertAtStart(30)
dll.insertAtStart(20)
dll.insertAtStart(10)

dll.printAll()

print(dll.getSize())

dll.insertAtEnd(40)
dll.insertAtEnd(50)
dll.insertAtEnd(60)

dll.printAll()

dll.printBackward()

dll.insert(6,80)

dll.printAll()

dll.printBackward()

dll.insertAtEnd(100)
dll.insertAtStart(0)

dll.printAll()

dll.printBackward()

print(dll.find(60))

dll.insertAfter(100,200)

dll.printAll()

dll.printBackward()

dll.insertList([300,400,500,600,700,800,900,1000])

dll.printAll()

dll.printBackward()

dll.removeByValue(1000)
dll.removeByValue(0)

dll.printAll()

dll.printBackward()

dll.insertAtStart(0)
dll.insertAtEnd(1000)

dll.printAll()

dll.printBackward()

dll.removeByIndex(0)
dll.removeByIndex(16)

dll.printAll()

dll.printBackward()