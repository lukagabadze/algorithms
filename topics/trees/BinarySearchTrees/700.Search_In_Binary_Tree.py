from utils import array_to_node_tree

class Solution(object):

  def searchBST(self, root, val):
    if root is None:
      return None
  
    if root.val == val:
      return root
  
    # Otherwise look for it either left or right, based on root.val and val
    if val < root.val:
      return self.searchBST(root.left, val)

    if val > root.val:
      return self.searchBST(root.right, val)


if __name__ == "__main__":
  solution = Solution()
  
  tree = [4, 2, 7, 1, 3]
  val = 2

  # tree = [15, 2, 25, 1, 3, 14, 26]
  # val = 14

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.searchBST(root, val)
  print("\n")
  print("answer: ", answer.val)