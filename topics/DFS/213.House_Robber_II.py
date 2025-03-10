from typing import List, Tuple
from functools import cache


"""
TIME: 3ms (Beats 10.77%)
Could be improved probably

NOTE: Yes, it can be VERY much improved by using dynamic programming,
but I used DFS just to learn DFS, I will solve it later using dynamic programming in the DP folder.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Case
        if len(nums) <= 3:
            return max(nums)

        @cache
        def rob_tuple(nums: Tuple[int], can_use_last: bool = True) -> int:
            # Base Case
            if len(nums) <= 1:
                return sum(nums)

            return max(nums[0] + rob_tuple(nums[2:]), nums[1] + rob_tuple(nums[3:]))

        # Same as House Robber I but with added handling outisde the DFS.
        return max(
            nums[0] + rob_tuple(tuple(nums[2 : len(nums) - 1])),
            nums[1] + rob_tuple(tuple(nums[3:])),
            nums[2] + rob_tuple(tuple(nums[4:])),
        )


if __name__ == "__main__":
    solution = Solution()

    # nums = [2, 3, 2]

    # nums = [1, 2, 3, 1]

    nums = [1, 2, 3]

    # nums = [1, 2, 9, 3]

    # nums = [5]

    # nums = [6, 6, 4, 8, 4, 3, 3, 10]

    print("nums: ", nums)
    print("\n")
    answer = solution.rob(nums)
    print("answer: ", answer)
