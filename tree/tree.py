class TreeNode:
    def __init__(self, data, designation=None):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent

        return level
                    
    def print_tree(self, type='name', level=0):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.get_level() > 0 else ""
        
        if type == 'name':
            print(prefix + str(self.data))
        elif type == 'designation':
            print(prefix + str(self.designation))
        elif type == 'both':
            print(prefix + f'{str(self.data)} ({str(self.designation)})')
        
        if self.children and self.get_level() < level:
            for child in self.children:
                child.print_tree(type, level)
                
if __name__ == "__main__":
    
    def build_tree():
        root = TreeNode("Electronics")
        
        laptop = TreeNode("Laptop")
        phone = TreeNode("Phone")
        tv = TreeNode("TV")
        
        laptop.add_child(TreeNode("Acer"))
        laptop.add_child(TreeNode("Vivobook"))
        laptop.add_child(TreeNode("HP"))
        
        phone.add_child(TreeNode("IPhone"))
        phone.add_child(TreeNode("Samsung"))
        phone.add_child(TreeNode("Nokia"))
        phone.add_child(TreeNode("Huawei"))
        
        tv.add_child(TreeNode("LG"))
        tv.add_child(TreeNode("Hisense"))
        
        root.add_child(laptop)
        root.add_child(tv)
        root.add_child(phone)
        
        return root
    
    root = build_tree()
    root.print_tree()