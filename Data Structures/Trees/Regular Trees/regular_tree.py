
"""
=================== Regular Trees ===================
Insertion Complexity:
Deletion Complexity:
Best for Heirarchal Structures

Each and every node is tree node itself

Each tree node has three class variables:
    parent: parent of current tree node
    data: the data in current tree node
    childern: [array] array of all childern (each child is tree node itself)

Methods:

addChild(data): add child to self
getLevel(): return level self
printAll(): print all tree nodes in heirarchical order
printByLevel(level): print tree until given order
getRoot(): return main root node of tree
getParent(data): get parent node of given data (if exist)

"""

class TreeNode:

    def __init__(self, data) -> None:
        self.parent = None
        self.childern = []
        self.data = data

    def addChild(self, data):

        data.parent = self
        self.childern.append(data)

    def getLevel(self):

        current_parent = self.parent
        count = 0
        while current_parent:
            current_parent = current_parent.parent
            count +=1

        return count
    
    def printAll(self):

        child_level = self.getLevel()
        print("   "*child_level+ "|----->>>>>> "+ self.data)

        if self.childern == []:
            return 

        for each_childern in self.childern:
            each_childern.printAll()

    def printByLevel(self, level):

        child_level = self.getLevel()
        if child_level <= level:
            print("   "*child_level + "|----->>>>>> "+ self.data)

        if self.childern:
            for each_child in self.childern:
                each_child.printByLevel(level)

    
    def search(self,value):

        if self.data == value:
            return True

        if self.childern == []:
            return 

        for each_childern in self.childern:
            x = each_childern.search(value)
            if x:
                return True

        return False

    def getRoot(self):

        current_tree_node = self

        while current_tree_node.parent:
            current_tree_node = current_tree_node.parent

        return current_tree_node.data


    def getParent(self,value):

        if self.childern == []:
            return 

        for each_childern in self.childern:
            if each_childern.data == value:
                return each_childern.parent.data
                

            y = each_childern.getParent(value)
            if y is not None:
                break

        if y:
            return y
        elif value == self.getRoot():
            return "Root Node has no parents!"
        
        
       


reg_tree = TreeNode("Habib University")

dsse = TreeNode("DSSE")
dsse.addChild(TreeNode("CS"))
dsse.addChild(TreeNode("CE"))
dsse.addChild(TreeNode("EE"))

ahss = TreeNode("AHSS")
ahss.addChild(TreeNode("SDP"))
ahss.addChild(TreeNode("CH"))
ahss.addChild(TreeNode("CND"))

reg_tree.addChild(dsse)
reg_tree.addChild(ahss)

reg_tree.printAll()

reg_tree.printByLevel(1)

print("CH exist: ",reg_tree.search("CH"))

print("Main root: ",reg_tree.getRoot())

print("CS Parent Root:",reg_tree.getParent("CS"))