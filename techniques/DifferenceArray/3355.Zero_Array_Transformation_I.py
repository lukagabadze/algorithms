from typing import List


class Solution(object):
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        subtraction_points = [0] * (len(nums) + 1)
        for left, right in queries:
            subtraction_points[left] += 1
            subtraction_points[right + 1] -= 1

        subtract = 0
        for i, num in enumerate(nums):
            subtract += subtraction_points[i]
            if num - subtract > 0:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 0, 1], [[0, 2]]),
        ([4, 3, 2, 1], [[1, 3], [0, 2]]),
        (
            [4, 3, 2, 1],
            [
                [0, 3],
                [0, 2],
                [0, 1],
                [0, 0],
            ],
        ),
        (
            [4, 3, 2, 1],
            [
                [0, 3],
                [0, 2],
                [0, 1],
            ],
        ),
    ]

    for nums, queries in q:
        print("nums: ", nums)
        print("queries:")
        for row in queries:
            print(row)
        print()
        answer = solution.isZeroArray(nums, queries)
        print("answer: ", answer)
        print("=====================")
        print()
