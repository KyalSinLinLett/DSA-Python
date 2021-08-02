class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert_node(self, data):
        
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.insert_node(data) # keep doing down until u reach the leaves
            else:
                self.left = BSTNode(data)
                
        else:
            if self.right:
                self.right.insert_node(data)
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
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # when node has no child -> just set it as none
            if self.left is None and self.right is None:
                return None
            
            # when node has only one child -> set the node as its left/right child node
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left 
            
            # when node has two children -> set node as the min of right subtree
            # min_node = self.right.find_min()
            # self.data = min_node
            # self.right = self.right.delete(min_node)
            
            # max of left subtree strategy - exercise BST2
            max_node = self.left.find_max()
            self.data = max_node
            self.left = self.left.delete(max_node)
            
        return self
        
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
        root.insert_node(elements[i])
        
    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.insert_node(45)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]


