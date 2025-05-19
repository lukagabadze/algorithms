"""
NOTE: Funny and kinda cool syntax of python:
    if nums[0] == nums[1] == nums[2]:
        return "equilateral"
"""

from typing import List


class Solution(object):
    def triangleType(self, nums: List[int]) -> str:
        # Triangle can not be assembled
        if (
            (nums[0] + nums[1] <= nums[2])
            or (nums[1] + nums[2] <= nums[0])
            or (nums[2] + nums[0] <= nums[1])
        ):
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"

        return "scalene"


if __name__ == "__main__":
    solution = Solution()

    q = [([3, 3, 3]), ([3, 4, 5]), ([1, 1, 100])]

    for arr in q:
        print("arr: ", arr)
        print()
        answer = solution.triangleType(arr)
        print("answer: ", answer)
        print("=====================")
        print()
