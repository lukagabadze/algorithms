from utils import array_to_node_tree, print_tree


"""
TIME: 0ms ez
"""


class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_node(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def get_min_node(self, root):
        if not root:
            return None

        left_min = self.get_min_node(root.left)
        right_min = self.get_min_node(root.right)

        min_node = root
        if left_min and left_min.val < min_node.val:
            min_node = left_min
        if right_min and right_min.val < min_node.val:
            min_node = right_min

        return min_node


if __name__ == "__main__":
    solution = Solution()

    # tree = [5, 3, 6, 2, 4, None, 7]
    # key = 3

    # tree = [4,2,7,1,3]
    # key = 2

    # tree = [4,2,7,1,3]
    # key = 0

    # tree = []
    # key = 0

    tree = [2, 3, 1]
    key = 2

    # tree = [3, 1, 4, None, 2]
    # key = 2

    # This testcase needs balancing after to become AVL Tree
    # tree = [5, 3, 6, None, 4, None, None]
    # key = 3

    root = array_to_node_tree(tree)
    print_tree(root)
    print("key: ", key)
    print("\n")
    new_root = solution.deleteNode(root, key)
    print("ANSWER: ")
    print_tree(new_root)
