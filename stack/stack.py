from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def __repr__(self):
        stk = ''
        
        for element in self.container:
            stk += str(element) + '-' if element != self.container[-1] else str(element) + '<-TOP'
        
        return stk
        
    def push(self, val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.size() <= 0
    
if __name__ == "__main__":
    print(__name__)