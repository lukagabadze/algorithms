from typing import List


class Solution(object):
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        answer = set()
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(i - k, 0), min(i + k + 1, n)):
                    answer.add(j)

        return list(answer)


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([3, 4, 9, 1, 3, 9, 5], 9, 1),
        ([2, 2, 2, 2, 2], 2, 2),
    ]

    for nums, key, k in q:
        print("nums: ", nums)
        print("key: ", key)
        print("k: ", k)
        print()
        print()
        answer = solution.findKDistantIndices(nums, key, k)
        print("answer: ", answer)
        print("=====================")
        print()
