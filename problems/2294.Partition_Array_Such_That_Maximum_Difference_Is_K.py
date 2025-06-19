from typing import List


class Solution(object):
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        nums = sorted(nums)
        n = len(nums)

        mn = nums[0]
        answer = 1
        for i in range(1, n):
            mx = nums[i]
            if mx - mn > k:
                mn = mx
                answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([3, 6, 1, 2, 5], 2),
        ([1, 2, 3], 1),
        ([2, 2, 4, 5], 0),
        ([2, 4, 2, 2, 5, 2], 2),
        ([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14),
    ]

    for nums, k in q:
        print("nums: ", nums)
        print("k: ", k)
        print()
        answer = solution.partitionArray(nums, k)
        print("answer: ", answer)
        print("=====================")
        print()
