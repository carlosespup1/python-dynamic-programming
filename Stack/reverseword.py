from stack import Stack

def reverse(str):
    s = Stack()
    str_reverse = ''
    for i in str:
        s.push(i)      
    while not s.is_empty():
        str_reverse += s.pop()
      
    return str_reverse

print(reverse('!evitacudE ot emocleW'))