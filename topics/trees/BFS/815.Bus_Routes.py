from collections import deque


"""
TIME: 91ms (Beats 84.14%)
NOTE: Much better than my previous method which only kept track of visited lines.
This time, I have visited_stops and visited_lines sets which help me avoid useless routes.
Also, I kept line indexes in the queue, now I keep stops.
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

        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_lines = set()
        while queue:
            (stop, ans) = queue.popleft()

            lines = bus_stop_map[stop]

            for line in lines:
                if line in visited_lines:
                    continue

                visited_lines.add(line)
                stops = routes[line]
                for stop in stops:
                    if stop == target:
                        return ans + 1
                    if stop not in visited_stops:
                        queue.append((stop, ans + 1))
                        visited_stops.add(stop)

        return -1


if __name__ == "__main__":
    solution = Solution()

    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6

    # routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    # source = 15
    # target = 12

    # routes = [[2], [2, 8]]
    # source = 8
    # target = 2

    print("routes: ", routes)
    print("source: ", source)
    print("target: ", target)
    print("\n")
    answer = solution.numBusesToDestination(routes, source, target)
    print("answer: ", answer)
