"""
NOTE: If a child goes below the "low" point, it can be safe to say that its left children will also go below "low", since node.left.val < node.val < low
Same thing with "high", if a node goes above the "high" value, its right children will also go above "high", since node.right.val > node.val > high

NOTE: While loops are necessary here!

TODO: Maybe I can simplify the code
"""


"""
TIME: 0ms
"""
class Solution(object):

  def trimBST(self, root, low, high):
    # Check for root and move onto 
    while (root and root.val is not None) and (root.val < low or root.val > high):
      if root.val < low:
        root = root.right

      if root.val > high:
        root = root.left

    return self.trim_subtree(root, low, high)
      
  def trim_subtree(self, root, low, high):
    if root is None:
      return None
  
    while(root.left and root.left.val is not None and root.left.val < low):
      root.left = root.left.right;

    while(root.right and root.right.val is not None and root.right.val > high):
      root.right = root.right.left;
  
    self.trim_subtree(root.left, low, high)
    self.trim_subtree(root.right, low, high)
    
    return root


if __name__ == "__main__":
  solution = Solution()
  
  tree = [3, 0, 4, None, 2, None, None, 1]
  low = 1
  high = 3

  # tree = [15, 2, 25, 1, 3, 14, 26]
  # val = 14

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.trimBST(root, low, high)
  print("\n")
  print("answer: ", answer)