"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

1) Create a root node whose value is the maximum value in nums.
2) Recursively build the left subtree on the subarray prefix to the left of the maximum value.
3) Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.
"""

from utils import TreeNode
from binary_tree_class import traverse


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        # if the array is empty
        if not nums:
            return None

        # Find the max value
        value = max(nums)
        index = nums.index(value)

        root = TreeNode(value)

        left_root = self.constructMaximumBinaryTree(nums[:index])
        right_root = self.constructMaximumBinaryTree(nums[index + 1 :])

        root.left = left_root
        root.right = right_root

        return root


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 1, 6, 0, 5]
    # nums = [3, 2, 1]

    print("nums: ", nums)
    print("\n")
    answer = solution.constructMaximumBinaryTree(nums)
    print()
    print("AFTER: ")
    traverse(answer)
    print()
