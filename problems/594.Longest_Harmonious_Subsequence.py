from typing import List
from collections import defaultdict


class Solution(object):
    def findLHS(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        answer = 0
        for n in nums:
            cnt[n] += 1

            if cnt[n - 1]:
                answer = max(answer, cnt[n] + cnt[n - 1])

            if cnt[n + 1]:
                answer = max(answer, cnt[n] + cnt[n + 1])

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 3, 2, 2, 5, 2, 3, 7]),
        ([1, 2, 3, 4]),
        ([1, 1, 1, 1]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.findLHS(nums)
        print("answer: ", answer)
        print("=====================")
        print()
