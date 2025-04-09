from utils import array_to_node_tree, print_tree


"""
OLD TIME: 7ms O(n)
I think this solution can be improved,
maybe stop when the pre_order array of nodes reaches the Kth element.

TIME: 0ms O(k)
I was right, but coding it was a little difficult so I took a look at solutions
and found a great submission by Sparsh, THANS! (https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/6362020/beats-super-easy-beginners-java-c-c-python-javascript-dart/)

It is still kind of O(n) but this time it's the worst case scenario,
since k <= n, O(k) is better.
"""


class Solution(object):
    count = 0

    def kthSmallest(self, root, k):
        if root is None:
            return None

        left_ans = self.kthSmallest(root.left, k)
        if left_ans is not None:
            return left_ans

        # Increment the value for current Node (in-order traversal)
        self.count += 1

        # Found the answer, return
        if k <= self.count:
            return root.val

        right_ans = self.kthSmallest(root.right, k)
        if right_ans is not None:
            return right_ans


if __name__ == "__main__":
    solution = Solution()

    # tree = [3, 1, 4, None, 2]
    # k = 1

    # tree = [5, 3, 6, 2, 4, None, None, 1]
    # k = 3

    # tree = [5, 3, 6, 2, 4, None, 7]
    # k = 6

    # tree = [4,2,7,1,3]
    # k = 2

    tree = [4, 2, 7, 0, 3]
    k = 1

    root = array_to_node_tree(tree)
    print_tree(root)
    print("k: ", k)
    print("\n")
    answer = solution.kthSmallest(root, k)
    print("answer: ", answer)
