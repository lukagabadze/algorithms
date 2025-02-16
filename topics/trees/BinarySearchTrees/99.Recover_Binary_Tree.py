"""
NOTE: Very similar to the previous problem 98.Validate_Binary_Tree
NOTE: IT was NOT FUCKING SIMILAR AT ALL. You need to use `In-Order` Traversal to fix this.
(There is also a fancy way using Morris Traversal, might code it after in-order solution)

NOTE:
Swapping two nodes:
At first, I though I would have to change the nodes with their children and parents two swap
But I joust figured out that I can just change their values, i might be stupid

NOTE:
I was thinking how would you find two misplaced values in a sorted array.
Then I figured it out, when you misplace two values in a sorted array:
1) One of the values becomes too small for its place
2) and another values becomes too big for its place
3) And the bigger one will ALWAYS come first, how amazing is that!

NOTE:
It's better to assemble in-order traversal array first
and then swap the values there, I think it's easier to understand.
Then as a bonus I can show how to do everything one single method.
"""


from utils import TreeNode, array_to_node_tree


"""
TIME: 8ms
Not optimal code for this solution, you can do this in one method
BUT, I think it's easier to understand for anyone wanting to learn
"""


class Solution(object):

    in_order_tree = []

    def recoverTree(self, root):
        # Very weird, without this line leetcode fails on this test `tree = [3, 1, 4, None, None, 2]`
        self.in_order_tree = []
        self.in_order_assemble(root)
        self.recover_in_order_bfs_array()
        # print([node.val for node in self.in_order_tree])

    def recover_in_order_bfs_array(self):
        first_anomaly_node = None
        second_anomaly_node = None

        for index, node in enumerate(self.in_order_tree):
            if index is 0:
                continue

            if not first_anomaly_node and self.in_order_tree[index - 1].val >= self.in_order_tree[index].val:
                first_anomaly_node = self.in_order_tree[index - 1]

            if first_anomaly_node and self.in_order_tree[index - 1].val >= self.in_order_tree[index].val:
                second_anomaly_node = self.in_order_tree[index]

        if first_anomaly_node and second_anomaly_node:
            first_anomaly_node.val, second_anomaly_node.val = second_anomaly_node.val, first_anomaly_node.val

    def in_order_assemble(self, root):
        if root is None:
            return True

        self.in_order_assemble(root.left)
        self.in_order_tree.append(root)
        self.in_order_assemble(root.right)


if __name__ == "__main__":
    solution = Solution()

    # tree = [1, 3, None, None, 2]
    tree = [3, 1, 4, None, None, 2]
    # tree = [4, 2, 7, 1, 3]

    # tree = [12, 4, 10, None, None, 6, 18, None, None, 5, 21]
    # tree = [8, 4, 13, 1, 11, 7, 18, None, None, None, None, None, None, 15, 21]

    root = array_to_node_tree(tree)

    print("tree: ", tree)
    print("\n")
    answer = solution.recoverTree(root)
    print("\n")
    print("answer: ", answer)
