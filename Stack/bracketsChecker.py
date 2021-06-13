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
    
    
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def balanced(str):
    stack = Stack()
    is_balanced = True
    index = 0
    
    while index < len(str) and is_balanced:
        parent = str[index]
        if parent in '({[':
            stack.push(parent)
        elif stack.is_empty():
            is_balanced = False
            break
        else:
            top = stack.pop()
            if not is_match(top, parent):
                is_balanced = False
                break
        index += 1
            
    if is_balanced and stack.is_empty():
        return True
    else:
        return False