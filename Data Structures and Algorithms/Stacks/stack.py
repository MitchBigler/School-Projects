class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            raise IndexError("empty stack")
        return self.items.pop()
    
    def top(self):
        if not self.items:
            raise IndexError("empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []