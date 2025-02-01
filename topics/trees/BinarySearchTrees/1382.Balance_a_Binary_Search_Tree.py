"""
NOTE: Just keep splitting the in_order_tree array in half.
Steps:
1) Assemble in_order_tree array which holds the nodes
2) Disassamble the tree, assign every left and right children to None
3) Recursively
---- 1) Choose root node, which is length // 2
---- 2) create left and right subtree, which are left_subtree = arr[:len(arr)], right_subtree = arr[len(arr)+1:]
---- 3) Assign left subtrees center node to root.left and right subtrees center node to root.right
---- 4) Run this function on left_subtree and right_subtree

I am the GOAT
"""


from utils import TreeNode, array_to_node_tree


"""
TIME: 63ms (Beats 92.66%)
MEMORY: 20.72MB (Beats 96.33%)
I might be the GOAT
"""
class Solution(object):

  def balanceBST(self, root):
    in_order_tree = []

    def build_in_order_tree_array(root):
      if root is None:
        return

      build_in_order_tree_array(root.left)
      in_order_tree.append(root)
      build_in_order_tree_array(root.right)

    build_in_order_tree_array(root)

    # Completely disassemble the binary search tree
    for node in in_order_tree:
      node.left = None
      node.right = None

    self.balance(in_order_tree)

    return in_order_tree[len(in_order_tree) // 2]
  
  def balance(self, in_order_tree):

    if not in_order_tree:
      return

    center_node_index = len(in_order_tree) // 2
    center_node = in_order_tree[center_node_index]

    left_subtree = in_order_tree[:center_node_index]
    right_subtree = in_order_tree[center_node_index + 1:]

    if left_subtree:
      center_node.left = left_subtree[len(left_subtree) // 2]

    if right_subtree:
      center_node.right = right_subtree[len(right_subtree) // 2]

    self.balance(left_subtree)
    self.balance(right_subtree)
  
    

if __name__ == "__main__":
  solution = Solution()
  
  # tree = [3, 0, 4, None, 2, None, None, 1]
  # tree = [1,None,2,None,3,None,4]
  tree = [1,None,15,14,17,7,None,None,None,2,12,None,3,9,None,None,None,None,11]

  # tree = [15, 2, 25, 1, 3, 14, 26]
  # val = 14

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.balanceBST(root)
  print("\n")
  print("answer: ", answer)