"""
NOTE: There must be a FAR FAR better way to do this, with a cleaner code.
TODO: Look into it.
"""


from utils import array_to_node_tree

class Solution(object):

  def isValidBST(self, root):
    (maximum, minimum, answer) = self.validate(root)
    return answer
    
  def validate(self, root):
    if root is None:
      return (None, None, True)
      
    (left_min, left_max, left_answer) = self.validate(root.left)
    (right_min, right_max, right_answer) = self.validate(root.right)

    new_min = min(root.val, left_min or float('inf'), right_min or float('inf'))
    new_max = max(root.val, left_max or float('-inf'), right_max or float('-inf'))

    if left_answer is False or right_answer is False:
      return (None, None, False)
    
    if (left_max is not None and left_max >= root.val) or (right_min is not None and right_min <= root.val):
      return (new_min, new_max, False)

    return (new_min, new_max, True)


    # print('root.val: ', root.val)
    # print('left_max: ', left_max)
    # print('right_min: ', right_min)
    # print('left_answer: ', left_answer)
    # print('right_answer: ', right_answer)
    # print()

if __name__ == "__main__":
  solution = Solution()
  
  # tree = [4, 2, 7, 1, 3]
  # tree = [5, 1, 4, None, None, 3, 6]
  # tree = [5, 4, 6, None, None, 3, 7]
  # tree = [15, 2, 25, 1, 3, 14, 26]
  # tree = [45, 42, None, None, 44, 43, None, 41]
  tree = [1, 0, 0]
  
  # tree = [5, 4, 10, None, None, 6, 9, None, None, 7, 12]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.isValidBST(root)
  print("\n")
  print("answer: ", answer)