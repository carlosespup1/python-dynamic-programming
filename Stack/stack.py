class Stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        return self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if self.items is not []:
            return self.items[-1]
        
    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items