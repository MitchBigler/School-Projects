'''Binary Search Tree ADT Class'''
from bst_node import BSTNode

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return self.root.show_tree()

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = BSTNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.left_child)
            else:
                currentNode.left_child = BSTNode(key, val, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = BSTNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)


    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, items):
        if node:
            self._inorder(node.left_child, items)
            items.append((node.key, node.value))
            self._inorder(node.right_child, items)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        if currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left_child)
        else:
            return self._get(key, currentNode.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)
    def is_empty(self):
        return not self.size
    def remove(self, currentNode):
        if currentNode.is_leaf():  # leaf
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        elif currentNode.has_bothChildren():  # interior
            succ = currentNode.right_child.find_min()
            succ.splice_out()
            currentNode.key = succ.key
            currentNode.value = succ.value

        else:  # this node has one child
            if currentNode.has_left_child():
                if currentNode.is_left_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.left_child
                elif currentNode.is_right_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.left_child
                else:
                    currentNode.replaceNodeData(
                        currentNode.left_child.key,
                        currentNode.left_child.value,
                        currentNode.left_child.left_child,
                        currentNode.left_child.right_child,
                    )
            else:
                if currentNode.is_left_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.right_child
                elif currentNode.is_right_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.right_child
                else:
                    currentNode.replaceNodeData(
                        currentNode.right_child.key,
                        currentNode.right_child.value,
                        currentNode.right_child.left_child,
                        currentNode.right_child.right_child,
                    )



def build_tree():
    mytree = BST()
    mytree[70] = "red"
    mytree[31] = "blue"
    mytree[93] = "yellow"
    mytree[14] = "at"
    mytree[50] = "uvu"
    mytree[35] = "cs"
    mytree[60] = "2420"
    mytree[55] = "data"
    return mytree

if __name__ == "__main__":

    mytree = build_tree()


    print(mytree[60])
    print(f'55 is in the tree: {55 in mytree}')
    print(f'100 is in the tree: {100 in mytree}')

    print(f'14: {mytree[14]}')
    print(f'31: {mytree[31]}')
    print(f'93: {mytree[93]}')

    print("Binary Search Tree:")
    print(mytree)

    print("Inorder traversal of the binary tree:")
    print(mytree.inorder())
    #
    del mytree[93]
    print("\ndelete nod 93")  # leaf node, is right child
    print(mytree)
    #
    print("Inorder traversal of the binary tree:")
    print(mytree.inorder())

    del mytree[31]
    print("\ndelete nod 31")  # has two children
    print(mytree)
    print(mytree.inorder())
    #
    del mytree[50]  # is right child, has right child
    print("\ndelete nod 50")
    print(mytree)
    print(mytree.inorder())

    #### MY METHODS ############################################################################

    def size(): #Return the number of nodes in the tree.
        return size

    def is_empty(): #Return True if there aren’t any nodes in the tree, False otherwise.
        return (size == 0)
    
    def height(): #Return the height of the tree, defined is the length of the path from the root to its deepest leaf. A tree with zero nodes has a height of -1.


    def add(item): #Add item to its proper place in the tree. Return the modified tree.

    def remove(item): #Remove item from the tree if it exists, if not – do nothing. Return the resulting tree. Note: when removing an item from the tree (if it isn't a leaf node which is trivial), the easiest thing to do is to replace the value in the node to be removed with either the rightmost value from the node's left subtree, or the leftmost value from the right subtree, and then remove the node whose value you "stole". Please note that our tests assume that you give precedence to the leftmost value from the right subtree.

    def find(item): #Return the matched item from the tree (not the node that contains it, and not the item used as the parameter). If item is not in the tree, raise a ValueError.

    def inorder(): #Return a list with the data items in order of inorder traversal.

    def preorder(self): #Return a list with the data items in order of preorder traversal.
        if self.root:
            items = []
            preorder(self.get_left_child()) + preorder(self.get_right_child())

            return items
        
    def postorder(): #Return a list with the data items in order of postorder traversal.

    def print_tree(): #print the values in the tree (in any way you wish). Useful for debugging purposes (a good example of this can be found in section 5.12.1 under the TreePrint.py file).