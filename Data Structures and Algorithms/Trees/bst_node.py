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

    def has_bothChildren(self):
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
                    self.parent.left_child = self.left_hild
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
    
