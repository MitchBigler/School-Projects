class BST:
    class BSTNode:
        def __init__(self,key,val,left=None,right=None, parent=None):
            # BSTNode(Pair(c), Pair(c))
            # A-z, 0-9
            self.key = key
            self.value = val
            self.left_child = left
            self.right_child = right
            self.parent = parent
            self.balance_factor = 0 # used to construct AVL tree

        def has_left_child(self):
            return self.left_child

        def has_right_child(self):
            return self.right_child

        def is_left_child(self):
            return self.parent and self.parent.left_child == self

        def is_right_child(self):
            return self.parent and self.parent.right_child == self

        def is_root(self):
            return not self.parent

        def is_leaf(self):
            return not (self.right_child or self.left_child)

        def has_anyChildren(self):
            return self.right_child or self.left_child

        def has_both_children(self):
            return self.right_child and self.left_child

        def replaceNodeData(self,key,value,lc,rc):
            self.key = key
            self.value = value
            self.left_child = lc
            self.right_child = rc
            if self.has_left_child():
                self.left_child.parent = self
            if self.has_right_child():
                self.right_child.parent = self

        def splice_out(self):
            if self.is_leaf():
                if self.is_left_child():
                    self.parent.left_child = None
                else:
                    self.parent.right_child = None
            elif self.has_anyChildren():
                if self.has_left_child():
                    if self.is_left_child():
                        self.parent.left_child = self.left_child
                    else:
                        self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    if self.is_left_child():
                        self.parent.left_child = self.right_child
                    else:
                        self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent

        def find_min(self):
            current = self
            while current.has_left_child():
                current = current.left_child
            return current

        def show_tree(self, level = 0):
            tree_str = f'|{"----|"*level}{self.key}\n'
            if self.left_child != None:
                left_c = self.left_child
                tree_str += left_c.show_tree(level+1)
            elif self.right_child != None:
                tree_str += f'|{"----|"*(level+1)}None\n'
            if self.right_child != None:
                right_c = self.right_child
                tree_str += right_c.show_tree(level+1)
            elif self.left_child != None:
                tree_str += f'|{"----|"*(level+1)}None\n'
            return tree_str

        def __str__(self):
            return self.key
    
    def __init__(self):
        self.root = None
        self.node_count = 0

    def __str__(self):
        return self.root.show_tree()

    def __len__(self):
        return self.node_count

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = BST.BSTNode(key, val)
        self.node_count += 1


    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.left_child)
            else:
                currentNode.left_child = BST.BSTNode(key, val, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = BST.BSTNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, items):
        if node:
            self._inorder(node.left_child, items)
            items.append(node.value)
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
        return self._get(key, self.root) is not None

    def remove(self, key):
        if self.node_count > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self.node_count -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.node_count == 1 and self.root.key == key:
            self.root = None
            self.node_count -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def _remove(self, currentNode):
        if currentNode.is_leaf():
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        elif currentNode.has_both_children():
            succ = currentNode.right_child.find_min()
            succ.splice_out()
            currentNode.key = succ.key
            currentNode.value = succ.value
        else:
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

    def find(self, item):
        node = self._get(item, self.root)
        if node:
            return node.value
        raise ValueError()

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.node_count == 0

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left_child)
        right_height = self._height(node.right_child)
        return 1 + max(left_height, right_height)

    def preorder(self):
        items = []
        self._preorder(self.root, items)
        return items

    def _preorder(self, node, items):
        if node:
            items.append(node.value)
            self._preorder(node.left_child, items)
            self._preorder(node.right_child, items)

    def postorder(self):
        items = []
        self._postorder(self.root, items)
        return items

    def _postorder(self, node, items):
        if node:
            self._postorder(node.left_child, items)
            self._postorder(node.right_child, items)
            items.append(node.value)

    def print_tree(self):
        print(self.inorder())


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
    del mytree[93]
    print("\ndelete node 93") 
    print(mytree)
    print("Inorder traversal of the binary tree:")
    print(mytree.inorder())
    del mytree[31]
    print("\ndelete node 31") 
    print(mytree)
    print(mytree.inorder())
    del mytree[50] 
    print("\ndelete node 50")
    print(mytree)
    print(mytree.inorder())
