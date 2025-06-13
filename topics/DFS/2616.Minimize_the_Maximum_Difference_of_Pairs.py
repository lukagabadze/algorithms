from typing import List


class Solution(object):
    def minimizeMax(self, nums: List[int], p: int) -> int:
        return self.find(sorted(nums), p)

    def find(self, nums: List[int], p: int) -> int:
        if p <= 0:
            return 0

        if len(nums) <= 1:
            return float("inf")

        return min(
            max(self.pair(nums[0], nums[1]), self.find(nums[2:], p - 1)),
            self.find(nums[1:], p),
        )

    def pair(self, num1: int, num2: int) -> int:
        return abs(num1 - num2)


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([10, 1, 2, 7, 1, 3], 2),
        ([4, 2, 1, 2], 1),
        ([8, 9, 1, 5, 4, 3, 6, 4, 3, 7], 4),
    ]

    for nums, p in q:
        print("nums: ", nums)
        print("p: ", p)
        print()
        answer = solution.minimizeMax(nums, p)
        print("answer: ", answer)
        print("=====================")
        print()
