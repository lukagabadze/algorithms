"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


NOTE
Good opportunity to explain map
I had no fucking clue it worked like that. Amazing!
map and list comprehension in one line, pretty cool!
"""

from utils import array_to_node_tree

class Solution(object):

  def binaryTreePaths(self, root):
    paths = self.find_paths(root)
    return ["->".join(map(str, reversed(path))) for path in paths]
    
  def find_paths(self, root):
    # Edge case
    if root is None:
      return []
    
    # We found a leaf, add it to the paths
    if root.left is None and root.right is None:
      return [[root.val]]
    
    # Otherwise find paths in left and right and append
    left_paths = self.find_paths(root.left)
    right_paths = self.find_paths(root.right)
    
    for i in range(len(left_paths)):
      left_paths[i].append(root.val)

    for i in range(len(right_paths)):
      right_paths[i].append(root.val)

    return left_paths + right_paths



if __name__ == "__main__":
  solution = Solution()
  
  # tree = [1, 2, 3, None, 5]
  # tree = [3, 9, 20, None, None, 15, 7];
  tree = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.binaryTreePaths(root)
  print("\n")
  print("answer: ", answer)