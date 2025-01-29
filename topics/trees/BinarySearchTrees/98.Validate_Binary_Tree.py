"""
NOTE: There must be a FAR FAR better way to do this, with a cleaner code.

CodingNinja has a great simple solution on leetcode: https://leetcode.com/problems/validate-binary-search-tree/solutions/5622933/video-check-range-of-each-node/
"""


from utils import array_to_node_tree

"""
TIME: 2ms (Thanks to CodingNinja!)
"""
class Solution(object):

  def isValidBST(self, root):
    # The root of the binary search tree can be whatever it wants, from -infinity to +infinity
    return self.validate(root, float("-inf"), float("inf"))
    
  def validate(self, root, minimum, maximum):
    if root is None:
      return True

    if root.val <= minimum or root.val >= maximum:
      return False

    # For left answer, the minimum stays the same, but the maximum value has become root.val (since root.left.val should definetely be under root.val)
    left_answer = self.validate(root.left, minimum, root.val)

    # For right answer, the maximum stays the same, but the minimum value has become root.val (since root.right.val should definetely be over root.val)
    right_answer = self.validate(root.right, root.val, maximum)

    return left_answer and right_answer

if __name__ == "__main__":
  solution = Solution()
  
  tree = [4, 2, 7, 1, 3]
  # tree = [5, 1, 4, None, None, 3, 6]
  # tree = [5, 4, 6, None, None, 3, 7]
  # tree = [15, 2, 25, 1, 3, 14, 26]
  # tree = [45, 42, None, None, 44, 43, None, 41]
  # tree = [1, 0, 0]
  
  # tree = [5, 4, 10, None, None, 6, 9, None, None, 7, 12]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.isValidBST(root)
  print("\n")
  print("answer: ", answer)