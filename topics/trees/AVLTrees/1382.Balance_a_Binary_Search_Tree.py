from utils import print_tree, array_to_node_tree

"""
NOTE: I have solved this problem the normal way, BUT
I want to solve it using AVL Trees now, just to learn about AVL Trees
"""
class Solution(object):

  def balanceBST(self, root):
    new_root = self.balance_using_avl(root)
    return new_root
  
  def balance_using_avl(self, root):
    if root is None:
      return
    
    # balance the subtrees first
    left = self.balance_using_avl(root.left)
    right = self.balance_using_avl(root.right)

    root.left = left
    root.right = right
    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    
    # balance factor
    bf = self.get_height(root.left) - self.get_height(root.right)

    # LL, Left-left, left heavy, perform right rotate
    if bf > 1 and self.get_height(root.left.left) >= self.get_height(root.left.right):
      return self.rotate_right(root)

    # RR, Right-right, right heavy, perform left rotate
    if bf < -1 and self.get_height(root.right.right) >= self.get_height(root.right.left):
      return self.rotate_left(root)

    # LR, Left-Right, left right heavy, perform left rotation and then right rotation
    if bf > 1 and self.get_height(root.left.right) > self.get_height(root.left.left):
      root.left = self.rotate_left(root.left)
      return self.rotate_right(root)
    
    # RL, Right-Left, right left heavy, perform right rotation and then left rotation
    if bf < -1 and self.get_height(root.right.left) > self.get_height(root.right.right):
      root.right = self.rotate_right(root.right)
      return self.rotate_left(root)


    # otherwise it's balanced, return the root
    return root

  def rotate_left(self, root):
    A = root
    B = root.right
    temp = B.left

    B.left = A
    A.right = temp

    A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
    B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))

    return B

  def rotate_right(self, root):
    A = root
    B = root.left
    temp = B.right

    B.right = A
    A.left = temp

    A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
    B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))

    return B
  
  def get_height(self, node):
    if node is None:
      return 0
    return node.height

    

if __name__ == "__main__":
  solution = Solution()
  
  # # Left heavy, tests right rotation
  # tree = [5, 3, None, 1]

  # # Right heavy, tests left rotation
  # tree = [9, None, 10, None, 11]

  # # Mix of Left heavy and right heavy
  # tree = [8, 5, 12, 3, None, 9, 16, 1, None, None, 10, None, None, None, None, None, 11]

  # LR, Left Right heavy
  # tree = [5, 1, None, None, 3]

  # RL, Right Left heavy
  # tree = [9, None, 11, 10]

  # Mix of LR and RL rotations
  # tree = [8, 5, 12, 1, None, 9, 16, None, 3, None, 11, None, None, None, None, 10]

  # tree = [3, 0, 4, None, 2, None, None, 1]
  # tree = [1,None,2,None,3,None,4]
  tree = [1,None,15,14,17,7,None,None,None,2,12,None,3,9,None,None,None,None,11]
  # tree = [15, 2, 25, 1, 3, 14, 26]

  # tree = [9, 2, 14, 1, 3, 11, 15, None, None, None, 7, None, 12, None, 17]

  root = array_to_node_tree(tree)

  print("BEFORE")
  print_tree(root)
  answer = solution.balanceBST(root)
  print("\n")
  print("AFTER")
  print_tree(answer)