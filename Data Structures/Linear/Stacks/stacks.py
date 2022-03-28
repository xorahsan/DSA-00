
"""
====================== STACKS =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: an array contains all items in stack

Methods:
push(value): push value to stack
pop(): return and remove top of stack
top(): return top value but not remove
isEmpty(): check whether the stack is empty or not and return True or False
printAll(): print the whole stack

"""

class Stack:

    def __init__(self) -> None:
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def isEmpty(self):
        return False if self.data else True 

    def printAll(self):
        stack_str = ''
        for elements in self.data[::-1]:
            x = str(elements)
            stack_str += " "+x
            print("|   "+ x + "   |")
        print(stack_str)



temp_stack = Stack()
temp_stack.push(8)
temp_stack.push(6)
temp_stack.push(5)
temp_stack.printAll()
print("Removed Item: ", temp_stack.pop())
temp_stack.printAll()
temp_stack.push(4)
temp_stack.push(3)
temp_stack.push(2)

temp_stack.printAll()
