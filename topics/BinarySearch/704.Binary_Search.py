from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 2),
    ]

    for nums, target in q:
        print("nums: ", nums)
        print("target: ", target)
        print()
        answer = solution.search(nums, target)
        print("answer: ", answer)
        print("=====================")
        print()
