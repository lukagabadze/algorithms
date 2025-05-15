from utils import TreeNode, print_tree
from typing import List, Optional


class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def assemble(arr: List[int]) -> Optional[TreeNode]:
            if not arr:
                return None

            n = len(arr)
            node = TreeNode(arr[n // 2])
            node.left = assemble(arr[: n // 2])
            node.right = assemble(arr[n // 2 + 1 :])
            return node

        return assemble(nums)


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([-10, -3, 0, 5, 9]),
        ([1, 3]),
    ]

    for arr in q:
        print("arr: ", arr)
        print()
        answer = solution.sortedArrayToBST(arr)
        print("answer:")
        print_tree(answer)
        print("=====================")
        print()
