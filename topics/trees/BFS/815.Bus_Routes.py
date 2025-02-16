from collections import deque


"""
TIME: 820ms (Beats 41.96%)
TODO: This can be improved, look into it
"""


class Solution:
    def numBusesToDestination(self, routes, source, target):
        # Base case
        if source == target:
            return 0

        bus_stop_map = {}
        for i, route in enumerate(routes):
            for bus_stop in route:
                if bus_stop not in bus_stop_map:
                    bus_stop_map[bus_stop] = [i]
                else:
                    bus_stop_map[bus_stop].append(i)

        if source not in bus_stop_map:
            return -1

        lines = bus_stop_map[source]

        queue = deque([(line, 1) for line in lines])
        visited = set(lines)
        answer = -1
        while queue:
            (line, ans) = queue.popleft()

            stops = routes[line]

            if target in stops:
                return ans

            for stop in stops:
                for stop_line in bus_stop_map[stop]:
                    if stop_line not in visited:
                        queue.append((stop_line, ans + 1))
                        visited.add(stop_line)

        return answer


if __name__ == "__main__":
    solution = Solution()

    # routes = [[1, 2, 7], [3, 6, 7]]
    # source = 1
    # target = 6

    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12

    # routes = [[2], [2, 8]]
    # source = 8
    # target = 2

    print("routes: ", routes)
    print("source: ", source)
    print("target: ", target)
    print("\n")
    answer = solution.numBusesToDestination(routes, source, target)
    print("answer: ", answer)
