"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum
of all left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
The rule is similar if the node does not have a right child.
"""


from utils import array_to_node_tree

"""
TIME: 7ms
"""
class Solution(object):

  def findTilt(self, root):
    (total_sum, answer) = self.recursive_tilt(root)
    return answer
  
  """
  This functions returns a tuple
  (total_sum, answer)
  
  total_sum - The sum of the subtree from the node (including the nodes value)
  answer - The sum of all tilt values, which is what we should return in the end
  """
  def recursive_tilt(self, node):
    
    if node is None:
      return (0, 0)
    
    (left_sum, left_answer) = self.recursive_tilt(node.left)
    (right_sum, right_answer) = self.recursive_tilt(node.right)
    
    tilt = abs(left_sum - right_sum)
    total_sum = left_sum + right_sum + node.val
    answer = left_answer + right_answer + tilt

    return (total_sum, answer)


if __name__ == "__main__":
  solution = Solution()
  
  # tree = [4, 2, 9, 3, 5, None, 7]
  tree = [21,7,14,1,1,2,2,3,3]

  root = array_to_node_tree(tree)
  
  print("tree: ", tree);
  print("\n")
  answer = solution.findTilt(root)
  print("\n")
  print("answer: ", answer)