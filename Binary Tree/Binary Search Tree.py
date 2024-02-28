# class Node:
#     def __init__(self, key) -> None:
#         """Constructor to create a new node
#             self.value is the stored value
#             self.left and self.right are the child nodes
#         Args:
#             key (int): Value to be stored
#         """
#         self.key = key
#         self.left = None
#         self.right = None

from dataclasses import dataclass
@dataclass
class Node:
    key: int
    left: 'Node' = None
    right: 'Node' = None

def insert(node: object, key: int) -> object:
    """Utility function to insert a new value (node) in the BST

    Args:
        node (object): The new node
        key (int): The value to be stored

    Returns:
        object: The new node
    """
    if node is None:
        # Tree is empty, so return a new node
        return Node(key)
    
    # Recurse down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
        
    return node


def search(root: object, key: int):
    # Base Cases: root is null or key is at root
    if root is None or root.key == key:
        return root
    
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)

def delete_node(root, key):
    # Base case
    if root is None:
        return root
    
    # Recurse to the node to be deleted
    
    if root.key > key:
        root.left = delete_node(root.left, key)
        return root
    elif root.key < key:
        root.right = delete_node(root.right, key)
        return root
    
    # Now we are at the node to be deleted
    
    # If one child is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
    
    # If both exist
    else:
        successor_parent = root
        
        # Find the successor
        succ = root.right
        while succ.left is not None:
            successor_parent = succ
            succ = succ.left
            
        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        
        if successor_parent != root:
            successor_parent.left = succ.right
        else:
            successor_parent.right = succ.right
            
        # Copy the value to root
        root.key = succ.key
        
        del succ
        return root
            
           
            
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.key, end=' ')
        in_order(node.right)        

def pre_order(node):
    if node is not None:
        print(node.key, end=' ')
        pre_order(node.left)
        pre_order(node.right)
        
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.key, end=" ")

if __name__ == '__main__':
    
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
 
    # Key to be found
    key = 6
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
 
    key = 60
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
        
    print(f'{in_order(root)=}')
    print(f'{pre_order(root)=}')
    print(f'{post_order(root)=}')
    
    
        # Let us create following BST
    #          50
    #       /     \
    #      30      70
    #     /  \    /  \
    #   20   40  60   80
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
 
    print("Original BST: ", end='')
    in_order(root)
 
    print("\n\nDelete a Leaf Node: 20")
    root = delete_node(root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    in_order(root)
 
    print("\n\nDelete Node with single child: 70")
    root = delete_node(root, 70)
    print("Modified BST tree after deleting single child Node:")
    in_order(root)
 
    print("\n\nDelete Node with both child: 50")
    root = delete_node(root, 50)
    print("Modified BST tree after deleting both child Node:")
    in_order(root)
    
