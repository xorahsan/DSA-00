
"""
=============== Binary Search Tree ==================
Search Complexity: O(logn)
insertion Complexity: O(logn)
deletion complexity: O(n)

Class variables:
    data: current node data
    left: subtree on left
    right: subtree on right

Methods:

addNode(data): add data to current tree according to ascesnding order
inOrderTraversal(): return sorted array of given tree (in order)
preOrderTraversal(): return pre order traversal array of given tree (pre order)
postOrderTraversal(): return post order traversal array of given tree (post order)
search(data): return True if given data exist in tree
min(): return minimum of tree
max(): return maximum of tree
calcSum(): return sum og tree

"""


class BinarySearchTree:

    def __init__(self, data = None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):

        if self.data == data:
            return

        if data < self.data:

            if self.left:
                
                self.left.addNode(data)

            else:
                self.left = BinarySearchTree(data)


            

        if data > self.data:

            if self.right:
                
                self.right.addNode(data)

            else:
                self.right = BinarySearchTree(data)


    def in_order_traversal(self):

        temp_arr = []

        if self.left:
            temp_arr = temp_arr + self.left.in_order_traversal()

        temp_arr = temp_arr + [self.data]

        if self.right:
            temp_arr = temp_arr + self.right.in_order_traversal()

        return temp_arr

    def pre_order_traversal(self):

        temp_arr = []

        temp_arr.append(self.data)

        if self.left:
            temp_arr += self.left.pre_order_traversal()

        if self.right:
            temp_arr+= self.right.pre_order_traversal()

        return temp_arr

    def post_order_traversal(self):

        temp_arr = []

        if self.left:
            temp_arr += self.left.post_order_traversal()

        if self.right:
            temp_arr += self.right.post_order_traversal()

        temp_arr.append(self.data)

        return temp_arr

    def search(self, value):

        if self.data == value:
            return True

        if value < self.data and self.left:

            return self.left.search(value)

        if value > self.data and self.right:

            return self.right.search(value)

        return False

    def min(self):

        if self.left:
            return self.left.min()

        return self.data

    def max(self):

        if self.right:
            return self.right.max()

        return self.data

    def calcSum(self):

        leftSum = 0
        if self.left:
            leftSum = self.left.calcSum()
            
        rightSum = 0
        if self.right:
            rightSum = self.right.calcSum()

        return leftSum + self.data + rightSum

    def deleteNode(self, value):

        if value < self.data:
            if self.left:
                self.left = self.left.deleteNode(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.deleteNode(value)

        else:

            if not self.right and not self.left:
                return None

            if not self.left:
                return self.right

            if not self.right:
                return self.left

            max_value = self.left.max()
            self.data = max_value
            self.left = self.left.deleteNode(max_value)

        return self
        


bst = BinarySearchTree(4)

bst.addNode(0)
bst.addNode(8)
bst.addNode(6)
bst.addNode(3)
bst.addNode(7)
bst.addNode(5)
bst.addNode(9) 
bst.addNode(7)   
bst.addNode(2)   
bst.addNode(1)        

# print(bst.search(9))
# print(bst.search(0))
# print(bst.search(4))
# print(bst.search(15))



print(bst.in_order_traversal())
print(bst.pre_order_traversal())
print(bst.post_order_traversal())
print("Minimum:",bst.min())
print("Maximum:",bst.max())
print("Sum:",bst.calcSum())

bst.deleteNode(9)

print(bst.in_order_traversal())