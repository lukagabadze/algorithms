
"""
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.


# NOTE
# Creating the answer array like this had an issue
# if I typed for example self.answer[0][0] = 999
# all the arrays in this matrix would have [0] equal to 999
# This happens because of how Python handles mutable objects like lists.
# When you use the * operator to create nested lists,
# the inner lists are references to the same list object.
# CODE: self.answer = [[""] * self.n] * self.m
"""

from utils import array_to_node_tree

class Solution(object):
    
  answer = []
  height = 0
  m = 0
  n = 0

  def printTree(self, root):
    self.height = self.find_height(root)
    self.m = self.height
    self.n = 2 ** (self.height) - 1
    
    # Create the empty answers array
    self.answer = [[""]  * self.n  for _ in range(self.m)] 
    
    # Fill the root in answer with r (row) and c (column)
    r = 0
    c = self.n // 2
    self.answer[r][c] = str(root.val)

    self.fill_answer(root, r, c)
    return self.answer

  def fill_answer(self, node, r, c):
    if node is None:
      return

    if node.left:
      left_r = r + 1
      left_c = c - 2 ** (self.m - r - 2)
      self.answer[left_r][left_c] = str(node.left.val)
      self.fill_answer(node.left, left_r, left_c)

    if node.right:
      right_r = r + 1
      right_c = c + 2 ** (self.m - r - 2)
      self.answer[right_r][right_c] = str(node.right.val)
      self.fill_answer(node.right, right_r, right_c)

    return

  def find_height(self, root):
    if root is None:
      return 0

    left_height = self.find_height(root.left)
    right_height = self.find_height(root.right)
    
    return max(left_height, right_height) + 1


if __name__ == "__main__":
  solution = Solution()
  
  tree = [1, 2, 3, None, 4]
  # tree = [1, 2, 3, None, 5]
  # tree = [3, 9, 20, None, None, 15, 7];
  # tree = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.printTree(root)
  print("\n")
  print("answer: ", answer)