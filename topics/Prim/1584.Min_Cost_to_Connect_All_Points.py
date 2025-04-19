from typing import List
from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        dists = [float("inf")] * n
        dists[0] = 0
        answer = 0
        while heap:
            distance, point_ind = heappop(heap)

            for i in range(n):
                if i == point_ind:
                    continue

                point_distance = abs(points[point_ind][0] - points[i][0]) + abs(
                    distance + points[point_ind][1] - points[i][1]
                )
                new_distance = point_distance

                # print("point_ind: ", point_ind)
                # print("i: ", i)
                # print("distance: ", distance)
                # print("point_distance: ", point_distance)
                # print("dists: ", dists)
                # print()

                if new_distance < dists[i]:
                    heappush(heap, (new_distance, i))
                    dists[i] = new_distance
                    answer += point_distance

        # print("dists: ", dists)
        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
        [[2, -3], [-17, -8], [13, 8], [-17, -15]],
    ]

    for points in q:
        print("points: ", *points)
        print()
        answer = solution.minCostConnectPoints(points)
        print("answer: ", answer)
        print("=====================")
        print()
