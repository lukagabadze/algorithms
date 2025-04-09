"""
NOTE: I am not sure if this DFS or not, I am really confused on what problems and solutions count as DFS.

NOTE: Gabo after one month here, this is a DFS, it's recursive DFS.
"""

from utils import array_to_node_tree, print_tree


class Solution(object):
    answer = None

    def lowestCommonAncestor(self, root, p, q):
        # Returns (p_exists, q_exists)
        def dfs(node):
            if node is None:
                return (False, False)

            (left_p_exists, left_q_exists) = dfs(node.left)
            (right_p_exists, right_q_exists) = dfs(node.right)

            p_exists = node == p or left_p_exists or right_p_exists
            q_exists = node == q or left_q_exists or right_q_exists

            if p_exists and q_exists and not self.answer:
                self.answer = node

            return (p_exists, q_exists)

        dfs(root)
        return self.answer


if __name__ == "__main__":
    solution = Solution()

    # tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # root = array_to_node_tree(tree)
    # p = root.left
    # q = root.right

    tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = array_to_node_tree(tree)
    p = root.left
    q = root.left.right.right

    print_tree(root)
    print("p: ", p.val)
    print("q: ", q.val)
    print("\n")
    answer = solution.lowestCommonAncestor(root, p, q)
    print("answer: ", answer.val)
