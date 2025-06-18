from typing import List


class Solution(object):
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)

        answer = []
        for i in range(0, n, 3):
            answer.append([nums[i], nums[i + 1], nums[i + 2]])

            if nums[i + 2] - nums[i] > k:
                return []

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2),
        ([2, 4, 2, 2, 5, 2], 2),
        ([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14),
    ]

    for nums, k in q:
        print("nums: ", nums)
        print("k: ", k)
        print()
        answer = solution.divideArray(nums, k)
        print("answer: ", answer)
        print("=====================")
        print()
