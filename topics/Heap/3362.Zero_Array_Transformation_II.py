"""
NOTE: HUGE thanks to Sung Jinwoo for the solution!
(https://leetcode.com/problems/zero-array-transformation-iii/solutions/6768535/priority-queues-in-depth-with-images-idea-behind-solution-c-python-java)

NOTE: Turns out I need more practice using heaps, I thought they would only be useful in graphs to find minimum distance in a weighted graph
but turns out there's more to heaps than I thought.
"""

from typing import List
from heapq import heappush, heappop


class Solution(object):
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = len(queries)

        # Sort the queries based on their start
        queries = sorted(queries, key=(lambda x: x[0]))

        # Queries we can use up
        available = []

        # Queries we committed and are still in our range
        assigned = []

        queries_committed = 0
        query_ind = 0

        for i in range(len(nums)):
            # Remove assigned queries based on i
            while assigned and assigned[0] < i:
                heappop(assigned)

            # Add new available queries based on i
            while query_ind < q and queries[query_ind][0] <= i:
                heappush(available, -queries[query_ind][1])
                query_ind += 1

            # Commit as much queries as we need to complete nums[i] (long queries first to cover more distance)
            while len(assigned) < nums[i] and available and -available[0] >= i:
                heappush(assigned, -heappop(available))
                queries_committed += 1

            # If we ever run out of available queries to cover nums[i], return -1, it's impossible to "zeroify" the array
            if len(assigned) < nums[i]:
                return -1

        return q - queries_committed


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([2, 0, 2], [[0, 2], [0, 2], [1, 1]]),
        ([1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]),
        ([1, 2, 3, 4], [[0, 3]]),
    ]

    for nums, queries in q:
        print("nums: ", nums)
        print("queries:")
        for row in queries:
            print(row)
        print()
        answer = solution.maxRemoval(nums, queries)
        print("answer: ", answer)
        print("=====================")
        print()
