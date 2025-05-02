"""
NOTE: This problem is NOT meant to be solved using DSU (Disjoint Set Union), I did it just to practice DSU.
If you want a solid O(n) solution without any fancy algorithms, here it is: https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak
"""

from typing import List
from collections import Counter


"""
TIME: 275ms (Beats 5.06%)
MEMORY: 48.63MB (Beats 5.16%)
"""


class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        parent = list(range(n))
        rank = [0] * n
        num_ind_map = {}

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1

        for i, num in enumerate(nums):
            # assign the num to num_ind_map
            if num not in num_ind_map:
                num_ind_map[num] = i
            else:
                continue

            points_of_interest = [num - 1, num + 1]
            for neighbour in points_of_interest:
                if neighbour in num_ind_map:
                    neighbour_ind = num_ind_map[neighbour]
                    union(i, neighbour_ind)

        counter = Counter([find(i) for i in parent])
        return counter.most_common()[0][1]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([100, 4, 200, 1, 3, 2]),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        ([1, 0, 1, 2]),
        ([]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.longestConsecutive(nums)
        print("answer: ", answer)
        print("=====================")
        print()
