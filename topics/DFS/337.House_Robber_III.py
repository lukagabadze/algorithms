from utils import TreeNode, array_to_node_tree, print_tree
from typing import Optional


"""
TIME: 3ms (Beats 87.88%)
Pretty Good!
"""


class Solution(object):
    def rob(self, root: Optional[TreeNode]) -> int:
        # DFS to traverse the tree.
        # Returns a tuple (includes, not_includes)
        # includes - Maximum subtree value which includes the root (of the subtree)
        # not_includes - Maximum subtree value which does NOT include the root (of the subtree)
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return (0, 0)

            (left_includes, left_not_includes) = dfs(node.left)
            (right_includes, right_not_includes) = dfs(node.right)

            includes = node.val + left_not_includes + right_not_includes
            not_includes = max(left_includes, left_not_includes) + max(
                right_includes, right_not_includes
            )

            return (includes, not_includes)

        (includes, not_includes) = dfs(root)
        return max(includes, not_includes)


if __name__ == "__main__":
    solution = Solution()

    # tree = [3, 2, 3, None, 3, None, 1]

    # tree = [3, 4, 5, 1, 3, None, 1]

    # tree = [5]

    tree = [4, 1, None, 2, None, 3]

    root = array_to_node_tree(tree)

    print_tree(root)
    print("\n")
    answer = solution.rob(root)
    print("\n")
    print("answer: ", answer)
