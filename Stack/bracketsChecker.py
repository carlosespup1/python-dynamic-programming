from stack import Stack
    
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