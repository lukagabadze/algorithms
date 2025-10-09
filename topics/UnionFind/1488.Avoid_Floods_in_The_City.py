from typing import List

"""
TIME: 307ms (Beats 6.48%)
NOTE: Initial solution using binary search.
This does not work because you can't remove an element from an array in O(logn) time.
Whereas in C++ for example, you can have std::set<int> s = {1, 3, 5, 7}; which is internally a balanced binary search tree.
so you can run binary search operations in O(logn) times and run element removal operations also in O(logn) time.
In python, this is not built-in, so you have to write this balanced binary search tree yourself.
Or, use a package like "sortedcontainers' which provides you with 'SortedList' for these operations.
I saw a solution on leetcode importing SortedList from sortedcontainers, so it is possible on leetcode.
TODO: Would be interesting to write this myself in python, meanwhile, I will solve this using Union Find.

TIME: 94ms (Beats 95.73%)
NOTE: Solved using Union Find, good explanation: "https://leetcode.com/problems/avoid-flood-in-the-city/solutions/7254853/avoid-flood-in-the-city-union-find-disjoint-set-optimal-solution-beginner-friendly".
This is not like other union find problems I have solved.
Instead of unioning a and b, we union a and a + 1.
What this means in this case is: "I am not a dry day and to dry me check the day on my right. (you can't dry a lake before theres rain in there)".
Then, when we go to that a + 1 day, if it's also a rain day, it will say the same, just join me with a + 1 + 1 and that might be a dry day.
So running find(i) gives you the index of the dry day that came after the rain at index i. WOW!
"""


class Solution(object):
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        parent = list(range(n + 1))
        
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node
        
        def union(a: int):
            parent[a] = a + 1
        
        lake = {}
        ans = [1] * n
        for i , r in enumerate(rains):
            if r != 0:
                ans[i] = -1
                union(i)
                
                if r in lake:
                    drain_ind = find(lake[r] + 1)

                    # No dry days between first (lake[r]) and the second (i) rain days on the same lake (r).
                    if drain_ind >= i:
                        return []
                    
                    ans[drain_ind] = r                    
                    lake[r] = i
                    
                    # We can't use this dry day anymore
                    union(drain_ind)
                else:
                    lake[r] = i
        
        return ans
        


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
        ([1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3]),
    ]

    for rains in q:
        print("rains: ", rains)
        print()
        answer = solution.avoidFlood(rains)
        print("answer: ", answer)
        print("=====================")
        print()
