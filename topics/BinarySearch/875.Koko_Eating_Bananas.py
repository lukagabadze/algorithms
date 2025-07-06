from typing import List


"""
TIME: 161ms (Beats 45.37%)
NOTE: This is my initial solution, using math.ceil to calculate hours.

TIME: 151ms (Beats 78.19%)
NOTE: Removing math.ceil call speeds up the solution by 10ms!! (Not much but cool).

NOTE: Also, this is how you remove math.ceil here:
    math.ceil(p / mid)

This, turns into this:
    (p + mid - 1) // mid

It gives the same result!
"""


class Solution(object):
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2

            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([3, 6, 7, 11], 8),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6),
    ]

    for nums, h in q:
        print("nums: ", nums)
        print("h: ", h)
        print()
        answer = solution.minEatingSpeed(nums, h)
        print("answer: ", answer)
        print("=====================")
        print()
