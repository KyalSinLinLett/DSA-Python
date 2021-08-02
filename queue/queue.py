from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1] if not self.isEmpty() else print("Queue is empty")
    
    def size(self):
        return len(self.buffer)
    
    def isEmpty(self):
        return self.size() <= 0     



