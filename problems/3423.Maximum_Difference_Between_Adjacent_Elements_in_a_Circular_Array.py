from typing import List


class Solution(object):
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])

        answer = float("-inf")
        for i in range(len(nums) - 1):
            answer = max(answer, abs(nums[i + 1] - nums[i]))

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 4]),
        ([-5, -10, -5]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.maxAdjacentDistance(nums)
        print("answer: ", answer)
        print("=====================")
        print()
