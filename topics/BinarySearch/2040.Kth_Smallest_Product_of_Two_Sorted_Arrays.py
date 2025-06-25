"""
NOTE: HUGE thanks to Dmitry for the explanation!
(https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/solutions/1524159/python-binary-search-solution-explained)

NOTE: I need to practice binary search a lot more, I am so fucking ass right now.

NOTE My intuition was correct which is great but I got stuck on implementation and time was running out,
so thanks to Dmitry I passed the daily challenge.
"""

from typing import List
from bisect import bisect, bisect_left
from math import ceil


class Solution(object):
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(x: int):
            total = 0

            for n1 in nums1:
                # If n1 is positive then "n1 * nums2" go in inscreasing order,
                # so we bisect to find number of values <= x // n1
                if n1 > 0:
                    total += bisect(nums2, x // n1)

                # If n1 is negative then "n1 * nums2" go in decreasing order
                # so we take the right path
                if n1 < 0:
                    total += len(nums2) - bisect_left(nums2, ceil(x / n1))

                # if n1 is equal to zero then "n1 * nums2" are all zeroes.
                if n1 == 0 and x >= 0:
                    total += len(nums2)

            return total

        left, right = -(10**10) - 1, 10**10 + 1
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([2, 5], [3, 4], 2),
        ([-4, -2, 0, 3], [2, 4], 6),
        ([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3),
    ]

    for nums1, nums2, k in q:
        print("nums1: ", nums1)
        print("nums2: ", nums2)
        print("k: ", k)
        print()
        answer = solution.kthSmallestProduct(nums1, nums2, k)
        print("answer: ", answer)
        print("=====================")
        print()
