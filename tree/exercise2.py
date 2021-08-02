# Now modify print_tree method to take tree level as input. 
# And that should print tree only upto that level as shown below,

from tree import TreeNode

def build_location_tree():
    global_ = TreeNode("global")
    
    india = TreeNode("india")
    usa = TreeNode("usa")
    
    gujarat = TreeNode("gujarat")
    karnataka = TreeNode("karnataka")
    newjersey = TreeNode("newjersey")
    california = TreeNode("california")
    
    ahmedabad = TreeNode("ahmedabad")
    baroda = TreeNode("baroda")
    bangluru = TreeNode("bangluru")
    mysore = TreeNode("mysore")
    princeton = TreeNode("princeton")
    trenton = TreeNode("trenton")
    sanfrancisco = TreeNode("sanfrancisco")
    mountainview = TreeNode("mountainview")
    pauloalto = TreeNode("pauloalto")

    
    global_.add_child(india)
    global_.add_child(usa)
    
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(newjersey)
    usa.add_child(california)

    california.add_child(sanfrancisco)
    california.add_child(mountainview)
    california.add_child(pauloalto)
    newjersey.add_child(trenton)
    newjersey.add_child(princeton)
    
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)
    
    return global_

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(level=1) # prints only name hierarchy
    root_node.print_tree(level=2) # prints only designation hierarchy
    root_node.print_tree(level=3) # prints both (name and designation) hierarchy