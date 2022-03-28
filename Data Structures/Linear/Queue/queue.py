

"""
====================== Queue =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: an array contains all items in queue

Methods:
enQueue(value): add data to queue
deQueue(): return and remove front of queue 
front(): return first queue value but not remove
isEmpty(): check whether the queue is empty or not and return True or False
printAll(): print the whole queue

"""

class Queue:

    def __init__(self) -> None:
        self.data = []

    def enQueue(self, value):
        self.data.append(value)

    def deQueue(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]

    def isEmpty(self):
        return False if self.data else True

    def printAll(self):

        for elements in self.data:
            print(" "+ str(elements)+ " | ", end='')


temp_queue = Queue()
temp_queue.enQueue(10)
temp_queue.enQueue(15)
temp_queue.enQueue(20)
print("Front:", temp_queue.front())
temp_queue.printAll()
print("Removed:",temp_queue.deQueue())
print("Front:", temp_queue.front())
temp_queue.printAll()