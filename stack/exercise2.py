# Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial. 

from stack import Stack

def is_balanced(string):
    
    s = Stack()

    for char in string:                 
        if char in ['{', '[', '(']:
            s.push(char)
            continue
            
        if char in ['}', ']', ')']:
            if s.isEmpty():
                return False
            
            if (s.peek() == "{" and char == '}') or (s.peek() == "(" and char == ')') or (s.peek() == "[" and char == ']'):
                s.pop()
                continue
                
    return s.isEmpty()

print(is_balanced("({a+b})"))   
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))    
print(is_balanced("))"))     
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
            
            
        
        
        