from typing import List


class Solution(object):
    nums = []
    cache = []

    def minimizeMax(self, nums: List[int], p: int) -> int:
        self.nums = sorted(nums)
        self.cache = [[[] for _ in range(p + 1)] for _ in nums]

        return self.find(0, p)

    def find(self, i: int, p: int) -> int:
        if p <= 0:
            return 0

        if i > len(self.nums) - 2:
            return float("inf")

        if self.cache[i][p]:
            return self.cache[i][p]

        answer = min(
            max(self.pair(self.nums[i], self.nums[i + 1]), self.find(i + 2, p - 1)),
            self.find(i + 1, p),
        )

        self.cache[i][p] = answer

        return answer

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
