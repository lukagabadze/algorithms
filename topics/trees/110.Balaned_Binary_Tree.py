"""
Given a binary tree, determine if it is height-balanced

Height-balanced:
A height-balanced binary tree is a binary tree in which
the depth of the two subtrees of every node never differs by more than one.

NOTE
I don't like using that extra find_tree_balance function,
but it's needed to return tuples with is_balanced and depth.

Maybe there is a way to put all the logic in isBalanced method
and returing a single boolean value.
"""

from utils import array_to_node_tree
from binary_tree_class import traverse

def find_tree_balance(root):
  if root is None:
    return (True, 0)
  
  if root.left is None and root.right is None:
    return (True, 1)
  
  # recursively check left and right child nodes
  (left_balanced, left_depth) = find_tree_balance(root.left)
  (right_balanced, right_depth) = find_tree_balance(root.right)

  balanced = (
    left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
  )
  depth = 1 + max(left_depth, right_depth)
  
  # Otherwise, the tree is balanced
  return (balanced, depth)


"""
Fast Solution where we pass the depth of the subtree to the parent
TIME: 3ms
NOTE: it still shows the 11ms result tho, which might be due to small range of n (0 <= n <= 5000)

"""
class Solution(object):
  def isBalanced(self, root):
    (is_tree_balanced, depth) = find_tree_balance(root)
    return is_tree_balanced


"""
Slower Solution where we calculate depth from every node
TIME: 11ms
"""
class SolutionSlow(object):
  def isBalanced(self, root):
    
    if root is None:
      return True

    left_depth = find_tree_depth(root.left)
    right_depth = find_tree_depth(root.right)

    difference = abs(left_depth - right_depth)
    is_balanced = difference <= 1
    
    return is_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
  solution = Solution()
  
  tree = [3, 9, 20, None, None, 15, 7];
  # tree = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.isBalanced(root)
  print("\n")
  print("answer: ", answer)