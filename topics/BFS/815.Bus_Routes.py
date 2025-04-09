from collections import deque


"""
First try:
TIME: 820ms (Beats 41.96%)

Second try:
TIME: 91ms (Beats 84.14%)
NOTE: Much better than my previous method which only kept track of visited lines.
This time, I have visited_stops and visited_lines sets which help me avoid useless routes.
Also, I kept line indexes in the queue, now I keep stops.

Third try:
TIME: 90ms (Beats 84.58%)
NOTE: This time, I put lines in the queue like in my first method,
BUT, I kept track of visited_stops alongside my ususal visited_lines
and the result is the same good performance.
Looks like the difference between 820ms and 90ms-91ms is just
keeping track of both visited lines and visited stops in a set.
"""


class Solution:
    def numBusesToDestination(self, routes, source, target):
        # Base case
        if source == target:
            return 0

        routes_set = [set(route) for route in routes]

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
        visited_lines = set(lines)
        visited_stops = set([source])
        while queue:
            (line, ans) = queue.popleft()

            if target in routes_set[line]:
                return ans

            stops = routes[line]

            for stop in stops:
                if stop in visited_stops:
                    continue

                visited_stops.add(stop)
                for stop_line in bus_stop_map[stop]:
                    if stop_line not in visited_lines:
                        queue.append((stop_line, ans + 1))
                        visited_lines.add(stop_line)

        return -1


if __name__ == "__main__":
    solution = Solution()

    # routes = [[1, 2, 7], [3, 6, 7]]
    # source = 1
    # target = 6

    # routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    # source = 15
    # target = 12

    routes = [[2], [2, 8]]
    source = 8
    target = 2

    print("routes: ", routes)
    print("source: ", source)
    print("target: ", target)
    print("\n")
    answer = solution.numBusesToDestination(routes, source, target)
    print("answer: ", answer)
