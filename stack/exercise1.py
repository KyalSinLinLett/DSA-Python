from stack import Stack
# reverse string using stack
string = "We will conquere COVID-19"

def reverse_string(string):
    s = Stack()
    for char in string:
        s.push(char)
        
    rev_s = ''
    while not s.isEmpty():
        rev_s += s.pop()
        
    return rev_s
   
print(reverse_string(string))
    
