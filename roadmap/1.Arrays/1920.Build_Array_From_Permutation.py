from typing import List

"""
TIME: 151ms (Beats 23.30%)
NOTE: Using only arrays this problem is slow O(n^2).
We can add a hash map to make it O(n).
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            count = 0

            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1

            ans.append(count)

        return ans


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([8, 1, 2, 2, 3]),
        ([6, 5, 4, 8]),
        ([7, 7, 7, 7]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.smallerNumbersThanCurrent(nums)
        print("answer: ", answer)
        print("=====================")
        print()
