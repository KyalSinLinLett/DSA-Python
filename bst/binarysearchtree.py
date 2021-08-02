class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data) # keep doing down until u reach the leaves
            else:
                self.left = BSTNode(data)
                
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
                
    def search(self, val):
        
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    # exercise1 
    def find_min(self):        
        if not self.left:
            return self.data
        
        return self.left.find_min()
    
    # exercise2
    def find_max(self):        
        if not self.right:
            return self.data
        
        return self.right.find_max()
    
    # calculate sum
    def calculate_sum(self):        
        return sum(self.in_order_traversal())
    
    # pre order traversal (BLR)
    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
                
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def in_order_traversal(self): # (LBR)
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    # post order traversal (LRB)
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
                
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
        
def build_tree(elements):
    root = BSTNode(elements[0])

    for i in range(len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__ == "__main__":

    numbers = [17, 4, 20, 9, 23, 18, 34, 1, 18, 4]
    number_tree = build_tree(numbers)
    
    print(number_tree.in_order_traversal())
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())

    print(number_tree.search(14))  
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.calculate_sum())
    
