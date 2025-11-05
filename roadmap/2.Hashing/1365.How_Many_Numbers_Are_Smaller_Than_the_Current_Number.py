from typing import List

"""
TIME: 3ms (Beats 72.87%)
NOTE: By counting the frequency of each element and summing the prefixes in sorted order
you get the result straight away. But my implementation is a lil dogshit, that's why i got 3ms instead of 1ms.

TIME: 4ms (Beats 61.80%)
NOTE: I cleaned up the code a lot, the performance difference is minimal,
it is way better to solve this problem like so: by sorting the array,
going through it and remembering the indexes in a hashmap.
(Don't forget that a single num can show up multiple times, hence `if num not in ans_map:`)
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(nums)

        ans_map = {}
        for ind, num in enumerate(snums):
            if num not in ans_map:
                ans_map[num] = ind

        return [ans_map[num] for num in nums]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([8, 1, 2, 2, 3]),
        ([6, 5, 4, 8]),
        ([7, 7, 7, 7]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.smallerNumbersThanCurrent(nums)
        print("answer: ", answer)
        print("=====================")
        print()
