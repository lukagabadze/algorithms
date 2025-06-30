"""
NOTE: Had no time today so I had to read the solution early!
HUGE thanks to varma_5247 for the solution!
(https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solutions/6896464/beginner-freindly-java-c-python-js)
"""

from typing import List


class Solution(object):
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Cache powers of 2 applied with MOD
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        answer = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                answer = (answer + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([3, 5, 6, 7], 9),
        ([3, 3, 6, 8], 10),
        ([2, 3, 3, 4, 6, 7], 12),
    ]

    for nums, k in q:
        print("nums: ", nums)
        print("k: ", k)
        print()
        answer = solution.numSubseq(nums, k)
        print("answer: ", answer)
        print("=====================")
        print()
