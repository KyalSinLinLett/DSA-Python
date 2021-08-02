from tree import TreeNode

def build_management_tree():
    nilupul = TreeNode("Nilupul", "CEO")
    
    chinmay = TreeNode("Chinmay", "CTO")
    gels = TreeNode("Gels", "HR Head")
    
    vishwa = TreeNode("Vishwa", "Infrastructure head")
    aamir = TreeNode("Aamir", "Application Head")
    peter = TreeNode("Peter", "Recruitment Manager")
    waqas = TreeNode("Waqas", "Policy Manager")
    
    dhaval = TreeNode("Dhaval", "Cloud Manager")
    abhijit = TreeNode("Abhijit", "Application Manager")
    
    nilupul.add_child(chinmay)
    nilupul.add_child(gels)
    
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)
    gels.add_child(peter)
    gels.add_child(waqas)
    
    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)
    
    return nilupul

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy