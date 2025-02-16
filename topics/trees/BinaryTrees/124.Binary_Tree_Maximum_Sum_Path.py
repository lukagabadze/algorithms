from utils import array_to_node_tree


class Solution(object):

    answer = float('-inf')

    def maxPathSum(self, root):
        self.find_max_subtrees(root)
        return self.answer

    def find_max_subtrees(self, root):
        if root is None:
            return 0

        left_max = self.find_max_subtrees(root.left)
        right_max = self.find_max_subtrees(root.right)

        self.answer = max(self.answer, root.val, root.val + left_max +
                          right_max, root.val + left_max, root.val + right_max)

        return max(root.val, root.val + left_max, root.val + right_max)


if __name__ == "__main__":
    solution = Solution()

    # tree = [1, 2, 3]
    tree = [-10, 9, 20, None, None, 15, 7]
    # tree = [5]
    # tree = [2, -1]
    # tree = [2, -1, -2]

    # tree = [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6]
    # tree = [4, 2, 9, 3, 5, None, 7]
    # tree = [21,7,14,1,1,2,2,3,3]

    root = array_to_node_tree(tree)

    print("tree: ", tree)
    print("\n")
    answer = solution.maxPathSum(root)
    print("\n")
    print("answer: ", answer)
