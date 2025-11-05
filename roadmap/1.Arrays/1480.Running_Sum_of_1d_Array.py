from typing import List


"""
TIME: 10ms (Beats 5.66%)
NOTE: This solution uses sum(nums[0:i+1]) to calculate the answer for each index, which is slow.
But its a good idea to show this solution and explain how we can make it faster.

TIME: 0ms (Beats 100%)
NOTE: By calculating new sum from the previous answer you get O(n) time instead of O(n^2).
"""


class Solution(object):
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        runningSum = [nums[0]]

        for i in range(1, n):
            new_sum = runningSum[-1] + nums[i]
            runningSum.append(new_sum)

        return runningSum


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 3, 4]),
        ([1, 1, 1, 1, 1]),
        ([3, 1, 2, 10, 1]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.runningSum(nums)
        print("answer: ", answer)
        print("=====================")
        print()
