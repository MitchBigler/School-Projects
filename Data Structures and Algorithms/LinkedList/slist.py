
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

        def __str__(self) -> str:
            return str(self.value)
        
        def __gt__(self, other):
            return self.value > other.value

    def __init__ (self):
        self._head = None
        self._size = 0

    def __iter__(self):
        self._current = self._head
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            value = self._current.value
            self._current = self._current.next
            return value

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        # Create a new obj of class SListNode that has the value of value
        new_node = self.SListNode(value)

        # New node is the head
        if self._head is None or new_node.value < self._head.value:
            new_node.next = self._head
            self._head = new_node
        # New node compared against next until less than or end
        else:
            # Set the new node between head and second item
            prev_node = self._head
            cur_node = self._head.next

            # While new node is greater than current's next node
            while cur_node is not None and new_node.value >= cur_node.value:
                prev_node = cur_node
                cur_node = cur_node.next
            
            prev_node.next = new_node
            new_node.next = cur_node
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        # Start at head
        cur_node = self._head

        while cur_node is not None:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False

    '''Remove the first occurance of value.'''
    def remove(self, value):
        cur_node = self._head

        if cur_node is not None and cur_node.value == value:
            self._head = cur_node.next
            return

        prev_node = None
        while cur_node is not None and cur_node.value != value:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        

    '''Remove all instances of value'''
    def remove_all(self, value):
        cur_node = self._head

        while cur_node is not None and cur_node.value == value:
            self._head = cur_node.next
            cur_node = self._head

        prev_node = None
        while cur_node is not None:
            if cur_node.value == value:
                prev_node.next = cur_node.next
            else:
                prev_node = cur_node
            cur_node = cur_node.next

    def size(self):
        return len(self)

    '''Convert the list to a string and return it'''
    def __str__(self):
        #Start at head
        cur_node = self._head
        stringResult = "["

        while cur_node is not None:
            stringResult += cur_node.__str__()
            stringResult += ","
            if cur_node.next is None:
                break
            cur_node = cur_node.next

        return stringResult + "]"

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        else:
            cur_node = self._head
            pos = 0
            while pos != index:
                if cur_node.next is None:
                    raise IndexError
                else:
                    pos += 1
                    cur_node = cur_node.next

            return cur_node

    def __len__(self):
        length = 0
        cur_node = self._head
        while cur_node is not None:
            length += 1
            cur_node = cur_node.next
        return length

    