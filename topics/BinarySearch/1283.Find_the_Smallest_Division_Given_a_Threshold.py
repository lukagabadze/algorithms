from typing import List


class Solution(object):
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2

            s = 0
            for n in nums:
                s += (n + mid - 1) // mid

            if s > threshold:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 5, 9], 6),
        ([44, 22, 33, 11, 1], 5),
    ]

    for nums, threshold in q:
        print("nums: ", nums)
        print("threshold: ", threshold)
        print()
        answer = solution.smallestDivisor(nums, threshold)
        print("answer: ", answer)
        print("=====================")
        print()
