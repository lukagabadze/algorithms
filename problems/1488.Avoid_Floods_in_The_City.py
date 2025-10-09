from typing import List
from collections import defaultdict
from bisect import bisect_right

"""
TIME: 307ms
NOTE: Initial solution with binary search
"""


class Solution(object):
    def avoidFlood(self, rains: List[int]) -> List[int]:
        m = len(rains)
        drain_inds = []

        # lake[r] holds index at which r was filled
        lake = defaultdict(lambda: -1)

        drains = [-1 for _ in range(m)]
        for i, r in enumerate(rains):
            if r == 0:
                drain_inds.append(i)
                drains[i] = 1
                continue

            if lake[r] != -1:
                if not drain_inds:
                    return []

                if drain_inds[-1] < lake[r]:
                    return []

                drain_ind = bisect_right(drain_inds, lake[r])
                drained = drain_inds.pop(drain_ind)
                drains[drained] = r

            lake[r] = i

        return drains


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 3, 4]),
        ([1, 2, 0, 0, 2, 1]),
        ([1, 2, 0, 1, 2]),
        ([69, 0, 0, 0, 69]),
        ([0, 1, 1]),
        ([1, 2, 0, 1]),
        ([1, 0, 2, 0, 2, 1]),
        ([1, 0, 2, 3, 0, 1, 2]),
        [1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3],
    ]

    for rains in q:
        print("rains: ", rains)
        print()
        answer = solution.avoidFlood(rains)
        print("answer: ", answer)
        print("=====================")
        print()
