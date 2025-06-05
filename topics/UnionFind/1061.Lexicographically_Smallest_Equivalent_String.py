"""
NOTE: I am so fucking goated 😭
I solved this with union find in 15 mins.
(we don't talk about the fact that it's slower than a dfs solution).
"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        m = 26
        parent = list(range(m))
        rank = [0] * m

        def find(node: int) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        def char_to_num(c: str) -> int:
            return ord(c) - ord("a")

        def num_to_char(num: int) -> str:
            return chr(num + ord("a"))

        for i in range(n):
            union(char_to_num(s1[i]), char_to_num(s2[i]))

        answer = ""
        for c in baseStr:
            c_num = char_to_num(c)
            equal = "a"
            for i in range(m):
                if find(c_num) == find(i):
                    equal = num_to_char(i)
                    break

            answer += equal

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("parker", "morris", "parser"),
        ("hello", "world", "hold"),
        ("leetcode", "programs", "sourcecode"),
    ]

    for s1, s2, baseStr in q:
        print("s1: ", s1)
        print("s2: ", s2)
        print("baseStr: ", baseStr)
        print()
        answer = solution.smallestEquivalentString(s1, s2, baseStr)
        print("answer: ", answer)
        print("=====================")
        print()
