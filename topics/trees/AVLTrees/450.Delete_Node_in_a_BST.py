"""
TODO: Solve this using the normal way as well.
It might be very very simple, just assign left or right child, or find minimum on the right, easy (maybe).
"""


from utils import TreeNode, array_to_node_tree, print_tree

class AVLTreeNode(object):
  def __init__(self, val=0, left=None, right=None, height=1):
    self.val = val
    self.left = left
    self.right = right
    self.height = height


"""
NOTE: This problem does NOT require AVL Trees,
I am using it just to learn about AVL Trees.
Normal way of solving this is much much faster, O(log(n)) I believe.

TIME: 313ms
Beats 6.04%
LMAO THIS IS SO SLOOOW but it's really beautiful 
"""
class Solution(object):
  def deleteNode(self, root, key):
    if root is None:
      return None
    
    root = self.assemble_avl_tree(root)
    
    # Delete the key node
    root = self.delete(root, key)
    
    # Turn back into TreeNode
    def convert(root):
      if root:
        return TreeNode(root.val, convert(root.left), convert(root.right))

    return convert(root)
  
  def assemble_avl_tree(self, root):
    def get_nodes(root):
      if root is None:
        return []
      return get_nodes(root.left) + get_nodes(root.right) + [root.val]
    
    nodes = get_nodes(root)
    root = None
    for node in nodes:
      root = self.insert(root, node)

    return root
  
  def delete(self, root, key):
    if root is None:
      return root
    elif key < root.val:
      root.left = self.delete(root.left, key)
    elif key > root.val:
      root.right = self.delete(root.right, key)
    else:
      # We have found the node to delete
      if not root.left:
        temp = root.right
        root = None
        return temp
      
      if not root.right:
        temp = root.left
        root = None
        return temp
      
      # The node has 2 children, find the minimum node that is larger than node.val
      # so we look in node.right
      temp = self.find_min_node(root.right)
      
      # Swap the values and delete the the min_node key
      root.val = temp.val
      root.right = self.delete(root.right, temp.val)
      
    # Since this leetcode problem does not require an AVL Tree to be returned
    # I can just leave the code like this and return unbalanced tree with deleted key node.
    # But, in order to learn about AVL Trees, let's balance the tree anyway
    
    # Update the height
    self.set_height(root)
    
    bf = self.get_balance_factor(root)
    
    if bf > 1 and self.get_balance_factor(root.left) >= 0:
      return self.rotate_right(root)
    
    if bf < -1 and self.get_balance_factor(root.right) <= 0:
      return self.rotate_left(root)
    
    if bf > 1 and self.get_balance_factor(root.left) < 0:
      root.left = self.rotate_left(root.left)
      return self.rotate_right(root)

    if bf < -1 and self.get_balance_factor(root.right) > 0:
      root.right = self.rotate_right(root.right)
      return self.rotate_left(root)

    # After all, return root
    return root


  def find_min_node(self, root):
    if not root:
      return None
    
    left_min_node = self.find_min_node(root.left)
    right_min_node = self.find_min_node(root.right)
    
    min_node = root

    if left_min_node and left_min_node.val < min_node.val:
      min_node = left_min_node

    if right_min_node and right_min_node.val < min_node.val:
      min_node = right_min_node
    
    return min_node

  
  def insert(self, root, val):
    if root is None:
      return AVLTreeNode(val)
    elif val < root.val:
      root.left = self.insert(root.left, val)
    elif val > root.val:
      root.right = self.insert(root.right, val)
      
    # Update the height
    self.set_height(root)

    # Balance Factor
    bf = self.get_balance_factor(root)
    
    # RR
    if bf > 1 and root.left.val > val:
      return self.rotate_right(root)
    
    # LL
    if bf < -1 and root.right.val < val:
      return self.rotate_left(root)
    
    # LR
    if bf > 1 and root.left.val < val:
      root.left = self.rotate_left(root.left)
      return self.rotate_right(root)
    
    # RL
    if bf < -1 and root.right.val > val:
      root.right = self.rotate_right(root.right)
      return self.rotate_left(root)

    return root
  
  def rotate_left(self, node):
    A = node
    B = node.right
    temp = B.left
    
    B.left = A
    A.right = temp
    
    self.set_height(A)
    self.set_height(B)
    
    return B

  def rotate_right(self, node):
    A = node
    B = node.left
    temp = B.right
    
    B.right = A
    A.left = temp
    
    self.set_height(A)
    self.set_height(B)
    
    return B
  
  def get_balance_factor(self, node):
    return 0 if not node else self.get_height(node.left) - self.get_height(node.right)
  
  def get_height(self, node):
    return 0 if not node else node.height
  
  def set_height(self, node):
    node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  


if __name__ == "__main__":
  solution = Solution()
  
  # tree = [5, 3, 6, 2, 4, None, 7]
  # key = 3
  
  # tree = [4,2,7,1,3]
  # key = 2

  # tree = [4,2,7,1,3]
  # key = 0

  # tree = []
  # key = 0
  
  # tree = [2, 3, 1]
  # key = 2
  
  # tree = [3, 1, 4, None, 2]
  # key = 2

  # This testcase needs balancing after to become AVL Tree
  tree = [5, 3, 6, None, 4, None, None]
  key = 3

  root = array_to_node_tree(tree)
  print_tree(root)
  print("key: ", key);
  print("\n")
  new_root = solution.deleteNode(root, key)
  print("ANSWER: ")
  print_tree(new_root)