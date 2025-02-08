from utils import array_to_node_tree, print_tree


"""
TIME: O(n) 7ms
I think this solution can be improved,
maybe stop when the pre_order array of nodes reaches the Kth element.
"""
class Solution(object):
  def kthSmallest(self, root, k):
    def get_pre_order_arr(root):
      if not root:
        return []
      return get_pre_order_arr(root.left) + [root.val] + get_pre_order_arr(root.right)

    sorted_nodes = get_pre_order_arr(root)
    filtered_nodes = [node for node in sorted_nodes if node is not None]

    return filtered_nodes[k - 1]


if __name__ == "__main__":
  solution = Solution()
  
  # tree = [3, 1, 4, None, 2]
  # k = 1
  
  # tree = [5, 3, 6, 2, 4, None, None, 1]
  # k = 3
  
  tree = [5, 3, 6, 2, 4, None, 7]
  k = 6
  
  # tree = [4,2,7,1,3]
  # k = 2

  root = array_to_node_tree(tree)
  print_tree(root)
  print("k: ", k);
  print("\n")
  answer = solution.kthSmallest(root, k)
  print("answer: ", answer)