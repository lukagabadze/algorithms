"""
NOTE: Huge thanks to KameshKadimisetty for the solution!
(https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/6491759/simple-dijkstra-s-algorithm-c)

NOTE: This solution is a bit different than the normal Dijkstra.
It goes to a certain node only if the price gets decreased.
And also, it uses the distance to sort the min_heap, not price which is very very interesting.
This way, we might see some nodes repeated in the heap, which is not something I saw in previous Dijsktra problems.

NOTE: I arrived at a problem "1928 Minimum Cost to Reach Destination in Time"
which is very very similar to this problem in the sense that you have to control 2 values:
Distance and Price.
I think I figured out why we put destination as the first element in the tuple of the priority queue.
The reason might be that after we check out all the possible paths whithin some destination,
we can just look into our answers array and find out the minimum cost it took to get to some node.
If the value of that itme is float('inf') than we know that you can not reach that node withing given max distance.

NOTE: I think this solution has a problem.
What if I like the new price and I update the prices dictionary,
but it turns out that distance + 1 is over the k limit and I ended up with
the lowest price but it does not fit in the k distance limit.
What the fuck...

NOTE: Finally starting to understand this implementation, why I need to update the prices dictionary
multiple times and not just once upon arriving at a node, like I have done in my previous Dijkstra implementations.
The answer is that previously I had "price" (for example) as my first element of the priority queue tuples.
It was sorted by price, so whenever I arrived at a node it was a FACT that that price was the lowest we could get.
But in this problem, you have another element called "distance".

NOW, you have 2 choices:
1) Sort the queue by price (by putting price as the first element) and finding that one lowest price
where the distance fits in the k limit.

OR

2) Sort the queue by distance, which will give you all the nodes with the lowest prices you can reach
within that distance. BUT, you WILL have to reassign the prices dictionary as you go and find new lower price paths.

Conclusion:
In this problems case, you need to sort the priority queue by the distance to not get TLE (Time Limit Exceeded).
Hence, you have to update the prices multiple times, but in the end, you can be sure
that if a node exists in the prices dictionary, it is the LOWEST price you can get in THAT DISTANCE.

NOTE: I noticed a potential gap in this solution, specifically in price dictionary assignment, where we don't check the distance and update
the price dictionary with the new lowest price. I though there would be an edge case where we update the prices dict, but the distance would go over the k limit.
So I just coded up a different type of solution where assignment of the prices dictionary happens right after the heap pops and we check for the distance.
It did not work at first, I then realized that we sort the priority queue by the distance, so the price might not be the lowest when we get to a certain node.
So I just added a min check `prices[node] = min(price, prices[node])`.
It still did NOT work.
I then figured out that this solution looks at STOPS and not DISTANCE.
To calculate stops from distance you need to subtract one from distance. So stops = distance - 1
So in the distance check I just needed to add `distance - 1 > k` to break.
This made the new solution work but if I were to go back to the older solution it would require me to update this distance check once more, back to `distance > k`.
So that's why it worked in the first place, because the difference between stops and distance were taken into consideration.
When I updated the prices dictionary every time I found a lower price path, there could NOT have been a case where the distance would be over the k limit.
If it were over the k limit, it would have been broken in the `distance > k` check.
Took me a week to understand but still pretty cool!

NOTE: This new solution is 6 times slower than the previous one.
I will still keep this soltuion here for reference but it should be noted that the previous one worked better for some reason.
Now I need to understand why that is... this never fucking stops...
"""

from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for node1, node2, price in flights:
            graph[node1].append((node2, price))

        heap = [(0, (0, src))]
        prices = defaultdict(lambda: float("inf"))
        while heap:
            (distance, (price, node)) = heappop(heap)

            if distance - 1 > k:
                break

            prices[node] = min(price, prices[node])

            for neighbour, n_price in graph[node]:
                if price + n_price < prices[neighbour]:
                    heappush(heap, (distance + 1, (price + n_price, neighbour)))

        if prices[dst] != float("inf"):
            return prices[dst]

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 2),
        (4, [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]], 0, 3, 0),
    ]

    for n, flights, src, dst, k in q:
        print("n: ", n)
        for row in flights:
            print(row)
        print("src: ", src)
        print("dst: ", dst)
        print("k: ", k)
        print()
        answer = solution.findCheapestPrice(n, flights, src, dst, k)
        print("answer: ", answer)
        print("=====================")
        print()
