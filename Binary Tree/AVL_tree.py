from dataclasses import dataclass

@dataclass
class AVL_Node(object):
    value: int
    left: 'AVL_Node' = None
    right: 'AVL_Node' = None
    height: int = 1
        
class AVL_Tree(object):
    def insert(self, root: 'AVL_Node', key: int):
        """Recursive function to insert key in  
           subtree rooted with node and returns 
           new root of subtree. 

        Args:
            root (AVL_Node): root of subtree
            key (int): Value sought
        """
        # Step 1