from typing import List


class Solution(object):
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        answer = -1
        for i in range(n):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    answer = max(answer, nums[j] - nums[i])

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([7, 1, 5, 4]),
        ([9, 4, 3, 2]),
        ([1, 5, 2, 10]),
    ]

    for n in q:
        print("n: ", n)
        print()
        answer = solution.maximumDifference(n)
        print("answer: ", answer)
        print("=====================")
        print()
