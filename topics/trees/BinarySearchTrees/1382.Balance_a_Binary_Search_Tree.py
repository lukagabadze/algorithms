from utils import TreeNode, array_to_node_tree

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

    print([node.val for node in in_order_tree])
    
    # Completely disassemble the binary search tree
    for node in in_order_tree:
      node.left = None
      node.right = None

    new_root_ind = len(in_order_tree) // 2
    new_root = in_order_tree[new_root_ind]

    # Split it down the middle
    left_half = list(reversed(in_order_tree[:new_root_ind]))
    right_half = in_order_tree[new_root_ind + 1:]

    # Initialize the root
    new_root.left = left_half[0]
    new_root.right = right_half[0]

    # Build the tree around the new root Left side
    for ind in range(len(left_half)):
      if ind == 0:
        continue
      left_half[ind - 1].left = left_half[ind]

    # Build the tree around the new root Right side
    for ind in range(len(right_half)):
      if ind == 0:
        continue
      right_half[ind - 1].right = right_half[ind]

    in_order_tree = []
    build_in_order_tree_array(new_root);
    print([node.val for node in in_order_tree])

    return new_root
  
    

if __name__ == "__main__":
  solution = Solution()
  
  # tree = [3, 0, 4, None, 2, None, None, 1]
  tree = [1,None,2,None,3,None,4]

  # tree = [15, 2, 25, 1, 3, 14, 26]
  # val = 14

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.balanceBST(root)
  print("\n")
  print("answer: ", answer)