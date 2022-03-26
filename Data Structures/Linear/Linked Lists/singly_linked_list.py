"""
======================= Singly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Node class Variables:
    value: value of current node
    next: whole next Node

Singly Linked List class variables:
    head: the whole node of current singly linked list head

Singly Linked List Methods:

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



"""




class Node: #for creating each Node
    def __init__(self,value= None,next = None):
        self.value = value
        self.next = next

class SinglyLinkedList: #linked list class in which we create nodes and link them

    def __init__(self) -> None:
        self.head = None # a whole node will be stored here

    def insertAtStart(self,value):
        temp_node = Node(value,self.head) #create node by assigning parameter value and add link to current head of linked list
        self.head = temp_node #assign current head to new Node

    def printAll(self): # print linked list

        currentNode = self.head #whole current node with two variables: value, next

        llstr = ''
        while currentNode: #until current node is not equal to None

            if currentNode.next == None:
                llstr = llstr+ str(currentNode.value)
            else:
                llstr = llstr+ str(currentNode.value) + "====>"

            currentNode = currentNode.next # change current node to next node by next variable of current node

        print(llstr)

    def getSize(self): #return length of linked list
        # total nodes = until current node is none

        count = 0
        currentNode = self.head

        while currentNode:
            count+=1
            currentNode = currentNode.next

        return count


    def insertAtEnd(self,data): #insert at the end of linked list
        
        if self.head == None:
            self.head = Node(data)

        currentNode = self.head
        while currentNode.next: # loop through all nodes until next node is none
            currentNode = currentNode.next
        currentNode.next = Node(data)
            
    def insert(self, index, data): #insert Node at given index

        if index < 0 or index > self.getSize(): #edge cases and exceptions
            raise Exception("Invaild Index")

        if index == 0: # we can't remove this because we used i = index -1
            self.insertAtStart(data)
            return

        i = 0
        currentNode = self.head
        while True: #break when index reached (it will defintely as code is exception handled)
            if i == index-1:
                temp_node = Node(data,currentNode.next)
                currentNode.next = temp_node
                break
            i = i+1
            currentNode = currentNode.next

        
    def removeByIndex(self,index): #remove Node by index

        if self.head is None:
            raise Exception("The linked list is empty")

        if index < 0 or index > self.getSize()-1:
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        i = 0
        currentNode = self.head
        while True: #break when index reached (it will defintely as code is exception handled)
            if i == index-1:
                currentNode.next = currentNode.next.next #currenNode.next is deleted here
                break
            i = i+1
            currentNode = currentNode.next
        
    def insertList(self,data_list): #insert Nodes in Bulk

        for data in data_list:
            self.insertAtEnd(data)

    def removeByValue(self,data): #remove Node by value

        if self.head is None:
            raise Exception("The linked list is empty")

        currentNode = self.head

        if currentNode.value == data:
            self.head = self.head.next
            return

        i,found = 0,False
        while i < self.getSize():
            if currentNode.next.value == data:
                currentNode.next,found = currentNode.next.next, True
                break
            i = i+1
            currentNode = currentNode.next

        if not found:
            print(f"{data} does not exist in the linked list!")


    def find(self,data): #return first index of given item

        if self.head is None:
            raise Exception("The linked list is empty")

        currentNode = self.head
        
        i = 0
        while i < self.getSize():
            if currentNode.value == data:
                return i
            i +=1
            currentNode = currentNode.next

        return "Not found"

    def insertAfter(self,after_value,data):
        
        # Method 01

        # if self.find(after_value) == "Not found" :
        #     raise Exception("The given after value does not exist!")

        # currentNode = self.head

        # while True:
        #     if currentNode.value == after_value:
        #         break
        #     currentNode = currentNode.next

        # temp_node = Node(data,currentNode.next)
        # currentNode.next = temp_node 

        # Method 02

        after_value_index = self.find(after_value)
        if after_value_index == "Not found" or self.head == None:
            raise Exception("The given after value does not exist!")
        self.insert(after_value_index+1,data)



            

ll1 = SinglyLinkedList()
ll1.insertAtStart(55)
ll1.insertAtStart(45)

# print(ll1.getSize())
# ll1.printAll()

ll1.insertAtEnd(75)

# ll1.printAll()

# print(ll1.getSize())

ll1.insert(2,70)

# ll1.printAll()

# print(ll1.getSize())

# ll1.remove(1)

ll1.insertList([100,120,150,160,190,200,250,300])

ll1.printAll()

ll1.removeByValue(45)

ll1.printAll()

print(ll1.find(160))

ll1.insertAfter(160, 180)

ll1.printAll()

ll1.insert(ll1.getSize(),55)


ll1.printAll()