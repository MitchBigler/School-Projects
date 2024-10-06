
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        # Create a new obj of class SListNode that has the value of value
        new_node = self.SListNode(value)

        # New node is the head
        if self._head == None or value < self._head:
            new_node.next = self._head
            self._head = new_node
        # New node is current and compared against next until less than or end
        else:
            current_node = self._head




    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        pass

    '''Remove the first occurance of value.'''
    def remove(self, value):
        pass

    '''Remove all instances of value'''
    def remove_all(self, value):
        pass

    '''Convert the list to a string and return it'''
    def __str__(self):
        pass

    '''Return an iterator for the list'''
    def __iter__(self):
        pass

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass
    