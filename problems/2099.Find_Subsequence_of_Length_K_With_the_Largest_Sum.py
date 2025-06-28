from typing import List


class Solution(object):
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest = sorted([(num, i) for i, num in enumerate(nums)])
        return [num for num, _ in sorted(largest[len(nums) - k :], key=lambda x: x[1])]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([2, 1, 3, 3], 2),
        ([-1, -2, 3, 4], 3),
        ([3, 4, 3, 3], 2),
        ([50, -75], 2),
    ]

    for nums, k in q:
        print("nums: ", nums)
        print("k: ", k)
        print()
        answer = solution.maxSubsequence(nums, k)
        print("answer: ", answer)
        print("=====================")
        print()
