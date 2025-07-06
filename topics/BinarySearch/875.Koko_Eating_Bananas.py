from typing import List
import math


class Solution(object):
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

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
